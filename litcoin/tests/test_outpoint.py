#!/usr/bin/env python3

from litcoin.binhex import b, x
from litcoin.uint256 import UINT256_SIZE_IN_BYTES, serialize_uint256
from litcoin.uint32 import UINT32_SIZE_IN_BYTES, serialize_uint32
from litcoin.outpoint import OUTPOINT_SIZE_IN_BYTES, validate_outpoint, make_outpoint, serialize_outpoint, \
    deserialize_outpoint, outpoint_to_human_readable, outpoint_copy
import unittest

TXID = 0x8000000000000000000000000000000000000000000000000000000000000001
OUTPUT_INDEX = 42


class TestOutpoint(unittest.TestCase):
    def test_OUTPOINT_SIZE_IN_BYTES(self):
        assert OUTPOINT_SIZE_IN_BYTES == UINT256_SIZE_IN_BYTES + UINT32_SIZE_IN_BYTES

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
        expected = serialize_uint256(TXID) + serialize_uint32(OUTPUT_INDEX)
        assert actual == expected

        with self.assertRaises(AssertionError, msg='should be raised because outpoint is invalid'):
            serialize_outpoint({})
    
    def test_deserialize_outpoint(self):
        data = serialize_uint256(TXID) + serialize_uint32(OUTPUT_INDEX)

        actual = deserialize_outpoint(data)[0]
        expected = {'txid': TXID, 'output_index': OUTPUT_INDEX}
        assert actual == expected

        with self.assertRaises(AssertionError, msg='should be raised because data is invalid'):
            data = b'\x00' * ((UINT256_SIZE_IN_BYTES + UINT32_SIZE_IN_BYTES) - 1)
            deserialize_outpoint(data)

    def test_outpoint_to_human_readable(self):
        actual = outpoint_to_human_readable(make_outpoint(TXID, OUTPUT_INDEX))
        expected = {'txid': TXID, 'output_index': OUTPUT_INDEX}
        assert actual == expected


    def test_outpoint_copy(self):
        original = make_outpoint(TXID, OUTPUT_INDEX)
        copy = outpoint_copy(original)

        assert type(copy) is type(original)
        assert sorted(copy.keys()) == sorted(original.keys())
        assert id(copy) != id(original)

        assert copy["txid"] == original["txid"]
        assert copy["output_index"] == original["output_index"]
