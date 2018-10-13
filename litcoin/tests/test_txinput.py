#!/usr/bin/env python3

from litcoin.outpoint import OUTPOINT_SIZE_IN_BYTES
from litcoin.uint32 import UINT32_SIZE_IN_BYTES
from litcoin.varint import VARINT_SIZE_RANGE_IN_BYTES
from litcoin.txinput import TXINPUT_SIZE_RANGE_IN_BYTES, make_txinput, validate_txinput, serialize_txinput, deserialize_txinput
import unittest


class TestTxinput(unittest.TestCase):
    def test_TXINPUT_SIZE_RANGE_IN_BYTES(self):
        assert TXINPUT_SIZE_RANGE_IN_BYTES == ( \
            OUTPOINT_SIZE_IN_BYTES + VARINT_SIZE_RANGE_IN_BYTES[0] + UINT32_SIZE_IN_BYTES \
        )

    def test_make_txinput(self):
        pass

    def test_validate_txinput(self):
        pass
    
    def test_serialize_txinput(self):
        pass
    
    def test_deserialize_txinput(self):
        pass
