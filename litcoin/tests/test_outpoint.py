#!/usr/bin/env python3

import unittest
from litcoin.binhex import b
from litcoin.uint32 import serialize_uint32
from litcoin.uint256 import serialize_uint256
from litcoin.outpoint import validate_outpoint, make_outpoint, serialize_outpoint, deserialize_outpoint

txid = 0x1000000000000000000000000000000000000000000000000000000000000001
output_index = 42

class TestOutpoint(unittest.TestCase):
    def test_validate_outpoint(self):
        validate_outpoint({'txid': txid, 'output_index': output_index})

    def test_make_outpoint(self):
        actual = make_outpoint(txid, output_index)
        expected = {'txid': txid, 'output_index': output_index}
        self.assertDictEqual(actual, expected)

        with self.assertRaises(TypeError, msg='should be raised because all arguments are missing'):
            make_outpoint()
        with self.assertRaises(TypeError, msg='should be raised because `output_index` argument is missing'):
            make_outpoint(txid)
        with self.assertRaises(AssertionError, msg='should be raised because `txid` argument is the wrong type'):
            make_outpoint(b('1000000000000000000000000000000000000000000000000000000000000001'), output_index)
        with self.assertRaises(AssertionError, msg='should be raised because `output_index` argument is the wrong type'):
            make_outpoint(output_index, 42.0)
        
    def test_serialize_outpoint(self):
        actual = serialize_outpoint({'txid': txid, 'output_index': output_index})
        expected = serialize_uint256(txid) + serialize_uint32(output_index)
        assert actual == expected
    
    def test_deserialize_outpoint(self):
        data = serialize_uint256(txid) + serialize_uint32(output_index)

        actual = deserialize_outpoint(data)
        expected = {'txid': txid, 'output_index': output_index}

        self.assertDictEqual(actual, expected)
