# returns hex value of a string with its length encoded
# in the beginning


def hexify(payload):
    """
        >> hexify('hello, world')
        >> Ox68656c6c6f2c20776f726c64a
    """

    delimited_payload = payload + '\n'
    if len(payload) == 0:
        return '0x0'

    payload_length = len(delimited_payload)
    payload_list = [ord(ch) for ch in delimited_payload]
    payload_hex = [format(val, 'x') for val in payload_list]
    payload_hex = ''.join(payload_hex)
    len_delimited_payload = hex(payload_length) + payload_hex
    return len_delimited_payload