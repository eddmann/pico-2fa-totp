import time
import json
import picodisplay as display
from totp import totp
from synchronised_time import create_synchronised_time

LED_BLINK_UNDER_SECONDS = 6


def hex_to_rgb(hex):
    return tuple(int(hex[i:i+2], 16) for i in (1, 3, 5))


codes = json.loads(open("codes.json", "r").read())
selected_idx = 0

display_width = display.get_width()
display_buffer = bytearray(display_width * display.get_height() * 2)
display.init(display_buffer)
display.set_backlight(0.8)

synchronised_time = create_synchronised_time(display)

while True:
    if display.is_pressed(display.BUTTON_X):
        selected_idx = (selected_idx + 1) % len(codes)

    code = codes[selected_idx]

    (password, expiry) = totp(synchronised_time(),
                              code['key'],
                              step_secs=code['step'],
                              digits=code['digits'])

    colour = hex_to_rgb(code['colour'])
    display.set_pen(*colour)
    display.clear()
    display.set_led(*colour
                    if expiry <= LED_BLINK_UNDER_SECONDS and expiry % 2
                    else (0, 0, 0))

    display.set_pen(0, 0, 0)
    display.text(code['name'], 10, 10, display_width - 10, 4)
    display.text(password, 10, 60, display_width - 10, 6)

    progress_width = display_width - \
        (display_width // code['step'] * (expiry - 1))
    display.rectangle(0, 125, progress_width, 10)

    display.update()
    time.sleep(0.5)
