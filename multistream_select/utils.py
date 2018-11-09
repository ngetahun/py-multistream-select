# returns hex value of a string with its length encoded
# in the beginning
from pyint import encode

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
    payload_hex_padded = [val if len(val) > 1 else '0'+val for val in payload_hex]
    payload_hex_padded = ''.join(payload_hex_padded)
    len_delimited_payload = "0x" + encode(payload_length, return_type="hex")[0] + payload_hex_padded
    return len_delimited_payload