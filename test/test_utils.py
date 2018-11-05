import pytest
from unittest import TestCase
from multistream_select import utils


class MultiStreamSelectUtilsTest(object):
    def setUp(self):
        pass

    @pytest.mark.parameterize(
        "test_in, test_out", [("hello, world", '0xd68656c6c6f2c20776f726c64a'),
                              ("na", '0x036e610a'), ("ls", '0x036c730a')])
    def TestHexify(self, test_in, test_out):
        assert utils.hexify(test_in) == test_out
