#!/usr/bin/env python3

import unittest
from litcoin.binhex import b
from litcoin.uint256 import UINT256_SIZE_IN_BYTES, serialize_uint256
from litcoin.uint32 import UINT32_SIZE_IN_BYTES, serialize_uint32
from litcoin.outpoint import OUTPOINT_SIZE_IN_BYTES, validate_outpoint, make_outpoint, serialize_outpoint, deserialize_outpoint

txid = 0x1000000000000000000000000000000000000000000000000000000000000001
output_index = 42

class TestOutpoint(unittest.TestCase):
    def test_OUTPOINT_SIZE_IN_BYTES(self):
        assert OUTPOINT_SIZE_IN_BYTES == UINT256_SIZE_IN_BYTES + UINT32_SIZE_IN_BYTES
    
    def test_validate_outpoint(self):
        validate_outpoint({'txid': txid, 'output_index': output_index})

        with self.assertRaises(AssertionError, msg='should be raised because `outpoint` has an extra unnecessary attribute'):
            validate_outpoint({'txid': txid, 'output_index': output_index, 'unnecessary_attribute': 42})
        with self.assertRaises(AssertionError, msg='should be raised because `outpoint.txid` is invalid'):
            validate_outpoint({'txid': -1, 'output_index': output_index})
        with self.assertRaises(AssertionError, msg='should be raised because `outpoint.output_index` is invalid'):
            validate_outpoint({'txid': txid, 'output_index': -1})
        with self.assertRaises(AssertionError, msg='should be raised because `outpoint` argument is missing `output_index` attribute'):
            validate_outpoint({'txid': txid})
        with self.assertRaises(AssertionError, msg='should be raised because `outpoint` argument is missing `txid` attribute'):
            validate_outpoint({'output_index': output_index})
        with self.assertRaises(AssertionError, msg='should be raised because `outpoint` argument is empty dict'):
            validate_outpoint({})
        with self.assertRaises(TypeError, msg='should be raised because all arguments are missing'):
            validate_outpoint()

    def test_make_outpoint(self):
        actual = make_outpoint(txid, output_index)
        expected = {'txid': txid, 'output_index': output_index}
        self.assertDictEqual(actual, expected)

        with self.assertRaises(AssertionError, msg='should be raised because `txid` argument is the wrong type'):
            make_outpoint(b('1000000000000000000000000000000000000000000000000000000000000001'), output_index)
        with self.assertRaises(AssertionError, msg='should be raised because `output_index` argument is the wrong type'):
            make_outpoint(output_index, 42.0)
        with self.assertRaises(TypeError, msg='should be raised because `output_index` argument is missing'):
            make_outpoint(txid)
        with self.assertRaises(TypeError, msg='should be raised because all arguments are missing'):
            make_outpoint()

    def test_serialize_outpoint(self):
        actual = serialize_outpoint({'txid': txid, 'output_index': output_index})
        expected = serialize_uint256(txid) + serialize_uint32(output_index)
        assert actual == expected
    
    def test_deserialize_outpoint(self):
        data = serialize_uint256(txid) + serialize_uint32(output_index)

        actual = deserialize_outpoint(data)
        expected = {'txid': txid, 'output_index': output_index}

        self.assertDictEqual(actual, expected)
