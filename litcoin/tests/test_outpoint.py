#!/usr/bin/env python3

from litcoin.binhex import b
from litcoin.txid import TXID_SIZE_IN_BYTES, serialize_txid
from litcoin.uint32 import UINT32_SIZE_IN_BYTES, serialize_uint32
from litcoin.outpoint import OUTPOINT_SIZE_IN_BYTES, validate_outpoint, make_outpoint, serialize_outpoint, deserialize_outpoint
import unittest

TXID = b('8000000000000000000000000000000000000000000000000000000000000001')
OUTPUT_INDEX = 42


class TestOutpoint(unittest.TestCase):
    def test_OUTPOINT_SIZE_IN_BYTES(self):
        assert OUTPOINT_SIZE_IN_BYTES == TXID_SIZE_IN_BYTES + UINT32_SIZE_IN_BYTES

    def test_make_outpoint(self):
        actual = make_outpoint(TXID, OUTPUT_INDEX)
        expected = {'txid': TXID, 'output_index': OUTPUT_INDEX}
        assert actual == expected

        with self.assertRaises(AssertionError, msg='should be raised because `txid` argument is the wrong type'):
            make_outpoint('wrong type', OUTPUT_INDEX)
        with self.assertRaises(AssertionError, msg='should be raised because `output_index` argument is the wrong type'):
            make_outpoint(TXID, 'wrong type')
        with self.assertRaises(TypeError, msg='should be raised because `output_index` argument is missing'):
            make_outpoint(TXID)
        with self.assertRaises(TypeError, msg='should be raised because all arguments are missing'):
            make_outpoint()

    def test_validate_outpoint(self):
        validate_outpoint({'txid': TXID, 'output_index': OUTPUT_INDEX})

        with self.assertRaises(AssertionError, msg='should be raised because `outpoint` has an extra unnecessary attribute'):
            validate_outpoint({'txid': TXID, 'output_index': OUTPUT_INDEX, 'unnecessary_attribute': 42})
        with self.assertRaises(AssertionError, msg='should be raised because `outpoint.txid` is invalid'):
            validate_outpoint({'txid': -1, 'output_index': OUTPUT_INDEX})
        with self.assertRaises(AssertionError, msg='should be raised because `outpoint.output_index` is invalid'):
            validate_outpoint({'txid': TXID, 'output_index': -1})
        with self.assertRaises(AssertionError, msg='should be raised because `outpoint.txid` is missing'):
            validate_outpoint({'output_index': OUTPUT_INDEX})
        with self.assertRaises(AssertionError, msg='should be raised because `outpoint.output_index` is missing'):
            validate_outpoint({'txid': TXID})
        with self.assertRaises(AssertionError, msg='should be raised because `outpoint` argument is empty dict'):
            validate_outpoint({})
        with self.assertRaises(TypeError, msg='should be raised because all arguments are missing'):
            validate_outpoint()

    def test_serialize_outpoint(self):
        actual = serialize_outpoint({'txid': TXID, 'output_index': OUTPUT_INDEX})
        expected = serialize_txid(TXID) + serialize_uint32(OUTPUT_INDEX)
        assert actual == expected

        with self.assertRaises(AssertionError, msg='should be raised because outpoint is invalid'):
            serialize_outpoint({})
    
    def test_deserialize_outpoint(self):
        data = serialize_txid(TXID) + serialize_uint32(OUTPUT_INDEX)

        actual = deserialize_outpoint(data)
        expected = {'txid': TXID, 'output_index': OUTPUT_INDEX}
        assert actual == expected

        with self.assertRaises(AssertionError, msg='should be raised because data is invalid'):
            data = b'\x00' * ((TXID_SIZE_IN_BYTES + UINT32_SIZE_IN_BYTES) - 1)
            deserialize_outpoint(data)
