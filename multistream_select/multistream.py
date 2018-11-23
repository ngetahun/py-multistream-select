import os  # noqa
import multiprocessing  # noqa
import io  # noqa
"""
    Implements the multistream select protocol multiplexer

    Usage
"""


class MultiStreamSelect(object):
    def __init__(self, proto):
        self.protocols = proto

    @property
    def protocols(self):
        # return a list of allowed protocols
        pass

    def add_protocol(self, protocol):
        # TODO: add more protocol validation
        if not isinstance(protocol, str):
            raise UnknownProtocol(protocol)

        if protocol in self.protocols:
            # raise ArgumentError()
            pass

    @property
    def codec(self):
        pass

    def validate_protocol_path(self):
        pass

    def handle(self):
        pass

    def __str__(self):
        pass


class UnknownProtocol(Exception):
    pass
