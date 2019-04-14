#!/usr/bin/env python3

from litcoin.binhex import b, x
from litcoin.uint256 import UINT256_SIZE_IN_BYTES, validate_uint256, serialize_uint256, deserialize_uint256, \
    uint256_to_hex, uint256_from_hex
import unittest


class TestUInt256(unittest.TestCase):
    def test_UINT256_SIZE_IN_BYTES(self):
        assert UINT256_SIZE_IN_BYTES == 32
    
    def test_validate_uint256(self):
        validate_uint256(0)
        validate_uint256(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff)

        with self.assertRaises(AssertionError, msg='should be raised because `n` argument is negative'):
            validate_uint256(-1)
        with self.assertRaises(AssertionError, msg='should be raised because `n` argument is too big for 256 bits'):
            validate_uint256(0x10000000000000000000000000000000000000000000000000000000000000000)
        with self.assertRaises(AssertionError, msg='should be raised because `n` argument is float'):
            validate_uint256(0.0)
        with self.assertRaises(AssertionError, msg='should be raised because `n` argument is the wrong type'):
            validate_uint256('wrong type')
        with self.assertRaises(TypeError, msg='should be raised because all arguments are missing'):
            validate_uint256()
    
    def test_serialize_uint256(self):
        assert serialize_uint256(0) == b('0000000000000000000000000000000000000000000000000000000000000000')
        assert serialize_uint256(1) == b('0100000000000000000000000000000000000000000000000000000000000000')
        assert serialize_uint256(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) == \
            b('ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff')
        assert serialize_uint256(0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe) == \
            b('feffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff')
    
        with self.assertRaises(AssertionError, msg='should be raised because `n` argument is negative'):
            serialize_uint256(-1)
        with self.assertRaises(AssertionError, msg='should be raised because `n` argument overflows to more than 256 bits'):
            serialize_uint256(0x10000000000000000000000000000000000000000000000000000000000000000)
        with self.assertRaises(AssertionError, msg='should be raised because `n` argument is of the wrong type'):
            serialize_uint256('wrong type')
        with self.assertRaises(TypeError, msg='should be raised because all arguments are missing'):
            serialize_uint256()
            
    def test_deserialize_uint256(self):
        assert deserialize_uint256(b('0000000000000000000000000000000000000000000000000000000000000000')) == \
            (0, 32)
        assert deserialize_uint256(b('0100000000000000000000000000000000000000000000000000000000000000')) == \
            (1, 32)
        assert deserialize_uint256(b('ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff')) == \
            (0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff, 32)
        assert deserialize_uint256(b('feffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff')) == \
            (0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe, 32)
        
        assert deserialize_uint256(b('0000000000000000000000000000000000000000000000000000000000000000'), 0) == \
            (0, 32)
        assert deserialize_uint256(b('0100000000000000000000000000000000000000000000000000000000000000'), 0) == \
            (1, 32)
        assert deserialize_uint256(b('ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff'), 0) == \
            (0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff, 32)
        assert deserialize_uint256(b('feffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff'), 0) == \
            (0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe, 32)
        
        assert deserialize_uint256(b('0000000000000000000000000000000000000000000000000000000000000000cc'), 0) == \
            (0, 32)
        assert deserialize_uint256(b('0100000000000000000000000000000000000000000000000000000000000000cc'), 0) == \
            (1, 32)
        assert deserialize_uint256(b('ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcc'), 0) == \
            (0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff, 32)
        assert deserialize_uint256(b('feffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcc'), 0) == \
            (0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe, 32)
          
        assert deserialize_uint256(b('cc0000000000000000000000000000000000000000000000000000000000000000'), 1) == \
            (0, 33)
        assert deserialize_uint256(b('cc0100000000000000000000000000000000000000000000000000000000000000'), 1) == \
            (1, 33)
        assert deserialize_uint256(b('ccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff'), 1) == \
            (0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff, 33)
        assert deserialize_uint256(b('ccfeffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff'), 1) == \
            (0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe, 33)
        
        assert deserialize_uint256(b('cc0000000000000000000000000000000000000000000000000000000000000000cc'), 1) == \
            (0, 33)
        assert deserialize_uint256(b('cc0100000000000000000000000000000000000000000000000000000000000000cc'), 1) == \
            (1, 33)
        assert deserialize_uint256(b('ccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcc'), 1) == \
            (0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff, 33)
        assert deserialize_uint256(b('ccfeffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcc'), 1) == \
            (0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe, 33)

        with self.assertRaises(AssertionError, msg='should be raised because `i` argument is negative'):
            deserialize_uint256(b('0000000000000000000000000000000000000000000000000000000000000000'), -1)
        with self.assertRaises(AssertionError, msg='should be raised because `data` argument is 31 bytes long'):
            deserialize_uint256(b('00000000000000000000000000000000000000000000000000000000000000'))
        with self.assertRaises(AssertionError, msg='should be raised because `i` argument is 0 when it should be 1 thus a different value is deserialized'):
            assert deserialize_uint256(b('cc0000000000000000000000000000000000000000000000000000000000000000'), 0) == 0
        with self.assertRaises(AssertionError, msg='should be raised because `i` argument is 2 when it should be 1 thus there\'s an overflow'):
            deserialize_uint256(b('cc0000000000000000000000000000000000000000000000000000000000000000'), 2)
        with self.assertRaises(AssertionError, msg='should be raised because `data` argument is of the wrong type'):
            deserialize_uint256('wrong type')
        with self.assertRaises(TypeError, msg='should be raised because all arguments are missing'):
            deserialize_uint256()

    def test_uint256_to_hex(self):
        actual = uint256_to_hex(0x055dd55091cf826f80f4a3fccef535378cc4d94b6609f60e4dbda9abeaa1801c)
        expected = "055dd55091cf826f80f4a3fccef535378cc4d94b6609f60e4dbda9abeaa1801c"
        assert actual == expected

        with self.assertRaises(AssertionError, msg="should be raised because `n` argument is too big for 256 bits"):
            uint256_from_hex(0x10000000000000000000000000000000000000000000000000000000000000000)
        with self.assertRaises(AssertionError, msg="should be raised because `s` argument is the wrong type"):
            uint256_to_hex("wrong type")
        with self.assertRaises(TypeError, msg="should be raised because all arguments are missing"):
            uint256_to_hex()


    def test_uint256_from_hex(self):
        actual = uint256_from_hex("055dd55091cf826f80f4a3fccef535378cc4d94b6609f60e4dbda9abeaa1801c")
        expected = 0x055dd55091cf826f80f4a3fccef535378cc4d94b6609f60e4dbda9abeaa1801c
        assert actual == expected

        with self.assertRaises(AssertionError, msg="should be raised because `s` argument has less than 64 characters"):
            uint256_from_hex("000000000000000000000000000000000000000000000000000000000000000")
        with self.assertRaises(AssertionError, msg="should be raised because `s` argument is too big for 256 bits"):
            uint256_from_hex("10000000000000000000000000000000000000000000000000000000000000000")
        with self.assertRaises(AssertionError, msg="should be raised because `s` argument is the wrong type"):
            uint256_from_hex("wrong type")
        with self.assertRaises(TypeError, msg="should be raised because all arguments are missing"):
            uint256_from_hex()
