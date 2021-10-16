def base32_decode(message):
    """
    Decodes the supplied encoded Base32 message into a byte string

    >>> base32_decode('DWRGVKRPQJLNU4GY')
    b'\\x1d\\xa2j\\xaa/\\x82V\\xdap\\xd8'
    >>> base32_decode('JBSWY3DPFQQHO33SNRSA====')
    b'Hello, world'
    """

    padded_message = message + '=' * (8 - len(message) % 8)
    chunks = [padded_message[i:i+8] for i in range(0, len(padded_message), 8)]

    decoded = []

    for chunk in chunks:
        bits = 0
        bitbuff = 0

        for c in chunk:
            if 'A' <= c <= 'Z':
                n = ord(c) - ord('A')
            elif '2' <= c <= '7':
                n = ord(c) - ord('2') + 26
            elif c == '=':
                continue
            else:
                raise ValueError("Not Base32")

            bits += 5
            bitbuff <<= 5
            bitbuff |= n

            if bits >= 8:
                bits -= 8
                byte = bitbuff >> bits
                bitbuff &= ~(0xFF << bits)
                decoded.append(byte)

    return bytes(decoded)
