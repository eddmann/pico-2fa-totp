import time


def create_synchronised_time(display):
    datetime = [2021, 1, 1, 1, 1, 0]
    selected_idx = 0

    display_width = display.get_width()
    display_height = display.get_height()

    while True:
        if display.is_pressed(display.BUTTON_A):
            selected_idx = (selected_idx + 1) % len(datetime)
        if display.is_pressed(display.BUTTON_X):
            datetime[selected_idx] += 1
        if display.is_pressed(display.BUTTON_Y):
            datetime[selected_idx] = max(datetime[selected_idx] - 1, 1)
        if display.is_pressed(display.BUTTON_B):
            break

        display.set_pen(0, 0, 0)
        display.clear()

        display.set_pen(255, 255, 255)

        display.text("Next", 10, 10, 30, 2)
        display.text("Inc", display_width - 40, 10, 30, 2)
        display.text("Dec", display_width - 40, display_height - 20, 30, 2)
        display.text("Confirm", 10, display_height - 20, 30, 2)

        display.text("YYYY MM DD HH MM SS", 30,
                     display_height // 2 - 10, display_width - 30, 2)
        display.text(
            " ".join("%s%02d" % (">" if idx == selected_idx else "", sep)
                     for idx, sep in enumerate(datetime)),
            30, display_height // 2 + 10, display_width - 30, 2)

        display.update()
        time.sleep(0.3)

    delta = time.mktime(datetime + [0, 0]) - int(time.time())

    def synchronised_time():
        return int(time.time()) + delta

    return synchronised_time
