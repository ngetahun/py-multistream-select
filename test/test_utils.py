import pytest
from multistream_select import utils

@pytest.mark.parametrize(
"test_in, test_out", [("hello, world", '0xd68656c6c6f2c20776f726c64a'),
                              ("na", '0x36e61a'), ("ls", '0x36c73a')])
def test_hexify(test_in, test_out):
    assert utils.hexify(test_in) == test_out
