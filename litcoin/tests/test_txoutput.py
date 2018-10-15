#!/usr/bin/env python3

from litcoin.uint64 import UINT64_SIZE_IN_BYTES
from litcoin.varint import VARINT_SIZE_RANGE_IN_BYTES
from litcoin.txoutput import TXOUTPUT_SIZE_RANGE_IN_BYTES, make_txoutput, validate_txoutput, serialize_txoutput, deserialize_txoutput
import unittest

VALUE = 42
LOCKING_SCRIPT = []


class TestTxoutput(unittest.TestCase):
    def test_TXOUTPUT_SIZE_RANGE_IN_BYTES(self):
        assert TXOUTPUT_SIZE_RANGE_IN_BYTES == ( \
            UINT64_SIZE_IN_BYTES + VARINT_SIZE_RANGE_IN_BYTES[0] \
        )

    def test_make_txoutput(self):
        actual = make_txoutput(VALUE, LOCKING_SCRIPT)
        expected = {'value': 42}

    def test_validate_txoutput(self):
        pass
    
    def test_serialize_txoutput(self):
        pass
    
    def test_deserialize_txoutput(self):
        #TODO - requires script deserialization
        pass
