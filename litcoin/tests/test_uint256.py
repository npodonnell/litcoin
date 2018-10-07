#!/usr/bin/env python3

import unittest
from litcoin.binhex import b, x
from litcoin.uint256 import serialize_uint256, deserialize_uint256


class TestUInt256(unittest.TestCase):
    def test_serialize_uint256(self):
        assert serialize_uint256(0) == b('0000000000000000000000000000000000000000000000000000000000000000')
        assert serialize_uint256(1) == b('0100000000000000000000000000000000000000000000000000000000000000')
        assert serialize_uint256(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) == b('ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff')
        assert serialize_uint256(0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe) == b('feffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff')
    
        with self.assertRaises(TypeError, msg='should be raised because all arguments are missing'):
            serialize_uint256()
        with self.assertRaises(AssertionError, msg='should be raised because `n` argument is negative'):
            serialize_uint256(-1)
        with self.assertRaises(AssertionError, msg='should be raised because `n` argument overflows to more than 256 bits'):
            serialize_uint256(0x10000000000000000000000000000000000000000000000000000000000000000)
        with self.assertRaises(AssertionError, msg='should be raised because `n` argument is of the wrong type'):
            serialize_uint256('wrong type')
    
    def test_deserialize_uint256(self):
        assert deserialize_uint256(b('0000000000000000000000000000000000000000000000000000000000000000')) == 0
        assert deserialize_uint256(b('0100000000000000000000000000000000000000000000000000000000000000')) == 1
        assert deserialize_uint256(b('ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff')) == 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        assert deserialize_uint256(b('feffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff')) == 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe
        
        assert deserialize_uint256(b('0000000000000000000000000000000000000000000000000000000000000000'), 0) == 0
        assert deserialize_uint256(b('0100000000000000000000000000000000000000000000000000000000000000'), 0) == 1
        assert deserialize_uint256(b('ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff'), 0) == 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        assert deserialize_uint256(b('feffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff'), 0) == 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe
        
        assert deserialize_uint256(b('0000000000000000000000000000000000000000000000000000000000000000cc'), 0) == 0
        assert deserialize_uint256(b('0100000000000000000000000000000000000000000000000000000000000000cc'), 0) == 1
        assert deserialize_uint256(b('ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcc'), 0) == 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        assert deserialize_uint256(b('feffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcc'), 0) == 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe
          
        assert deserialize_uint256(b('cc0000000000000000000000000000000000000000000000000000000000000000'), 1) == 0
        assert deserialize_uint256(b('cc0100000000000000000000000000000000000000000000000000000000000000'), 1) == 1
        assert deserialize_uint256(b('ccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff'), 1) == 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        assert deserialize_uint256(b('ccfeffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff'), 1) == 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe
        
        assert deserialize_uint256(b('cc0000000000000000000000000000000000000000000000000000000000000000cc'), 1) == 0
        assert deserialize_uint256(b('cc0100000000000000000000000000000000000000000000000000000000000000cc'), 1) == 1
        assert deserialize_uint256(b('ccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcc'), 1) == 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        assert deserialize_uint256(b('ccfeffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcc'), 1) == 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe
        
        with self.assertRaises(TypeError, msg='should be raised because all arguments are missing'):
            deserialize_uint256()
        with self.assertRaises(AssertionError, msg='should be raised because `data` argument is of the wrong type'):
            deserialize_uint256('wrong type')
        with self.assertRaises(AssertionError, msg='should be raised because `i` argument is negative'):
            deserialize_uint256(b('0000000000000000000000000000000000000000000000000000000000000000'), -1)
        with self.assertRaises(AssertionError, msg='should be raised because `data` argument is 31 bytes long'):
            deserialize_uint256(b('00000000000000000000000000000000000000000000000000000000000000'))
        with self.assertRaises(AssertionError, msg='should be raised because `i` argument is 0 when it should be 1 thus a different value is deserialized'):
            assert deserialize_uint256(b('cc0000000000000000000000000000000000000000000000000000000000000000'), 0) == 0
        with self.assertRaises(AssertionError, msg='should be raised because `i` argument is 2 when it should be 1 thus there\'s an overflow'):
            deserialize_uint256(b('cc0000000000000000000000000000000000000000000000000000000000000000'), 2)
