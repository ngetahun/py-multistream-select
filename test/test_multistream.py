from unittest import TestCase
from multistream_select import MultiStreamSelect as mss


class MultiStreamSelectTest(TestCase):
    def setUp(self):
        self._mss = mss(["/v", "/w", "/x"])

    # def TestRemoveProtocol(self):
    #     proto = "/v"
    #     self._mss.remove_protocol(proto)
    #     self.assertEqual(self._mss.protocols, ["/w", "/x"])

    # def TestHandler(self):
    #     def handler(p, err):

    def tearDown(self):
        pass