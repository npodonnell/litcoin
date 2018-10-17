#!/usr/bin/env python3

import unittest
from litcoin.binhex import b, x
from litcoin.varint import VARINT_SIZE_RANGE_IN_BYTES, validate_varint, serialize_varint, deserialize_varint


class TestVarInt(unittest.TestCase):
    def test_VARINT_SIZE_RANGE_IN_BYTES(self):
        assert VARINT_SIZE_RANGE_IN_BYTES == (1, 9)
    
    def test_validate_varint(self):
        validate_varint(0)
        validate_varint(0xffffffffffffffff)

        with self.assertRaises(AssertionError, msg='should be raised because `n` argument is negative'):
            validate_varint(-1)
        with self.assertRaises(AssertionError, msg='should be raised because `n` argument is too big for 256 bits'):
            validate_varint(0x10000000000000000)
        with self.assertRaises(AssertionError, msg='should be raised because `n` argument is float'):
            validate_varint(0.0)
        with self.assertRaises(AssertionError, msg='should be raised because `n` argument is the wrong type'):
            validate_varint('wrong type')
        with self.assertRaises(TypeError, msg='should be raised because all arguments are missing'):
            validate_varint()
    
    def test_serialize_varint(self):
        assert serialize_varint(0) == b'\x00'
        assert serialize_varint(1) == b'\x01'
        assert serialize_varint(251) == b'\xfb'
        assert serialize_varint(252) == b'\xfc'
        assert serialize_varint(253) == b'\xfd\xfd\x00'
        assert serialize_varint(254) == b'\xfd\xfe\x00'
        assert serialize_varint(255) == b'\xfd\xff\x00'
        assert serialize_varint(256) == b'\xfd\x00\x01'
        assert serialize_varint(65535) == b'\xfd\xff\xff'
        assert serialize_varint(65536) == b'\xfe\x00\x00\x01\x00'
        assert serialize_varint(4294967295) == b'\xfe\xff\xff\xff\xff'
        assert serialize_varint(4294967296) == b'\xff\x00\x00\x00\x00\x01\x00\x00\x00'
        assert serialize_varint(0xffffffffffffffff) == b'\xff\xff\xff\xff\xff\xff\xff\xff\xff'

        with self.assertRaises(AssertionError, msg='should be raised because `n` argument is negative'):
            serialize_varint(-1)
        with self.assertRaises(AssertionError, msg='should be raised because `n` argument overflows to more than 64 bits'):
            serialize_varint(0x10000000000000000)
        with self.assertRaises(AssertionError, msg='should be raised because `n` argument is of the wrong type'):
            serialize_varint('wrong type')
        with self.assertRaises(TypeError, msg='should be raised because all arguments are missing'):
            serialize_varint()

    def test_deserialize_varint(self):
        assert deserialize_varint(b('00')) == (0, 1)
        assert deserialize_varint(b('01')) == (1, 1)
        assert deserialize_varint(b('fb')) == (251, 1)
        assert deserialize_varint(b('fc')) == (252, 1)
        assert deserialize_varint(b('fdfd00')) == (253, 2)
        assert deserialize_varint(b('fdfe00')) == (254, 2)
        assert deserialize_varint(b('fdff00')) == (255, 2)
        assert deserialize_varint(b('fd0001')) == (256, 2)
        assert deserialize_varint(b('fdffff')) == (65535, 2)
        assert deserialize_varint(b('fe00000100')) == (65536, 4)
        assert deserialize_varint(b('feffffffff')) == (4294967295, 4)
        assert deserialize_varint(b('ff0000000001000000')) == (4294967296, 8)
        assert deserialize_varint(b('ffffffffffffffffff')) == (0xffffffffffffffff, 8)
        
        assert deserialize_varint(b('00'), 0) == (0, 1)
        assert deserialize_varint(b('01'), 0) == (1, 1)
        assert deserialize_varint(b('fb'), 0) == (251, 1)
        assert deserialize_varint(b('fc'), 0) == (252, 1)
        assert deserialize_varint(b('fdfd00'), 0) == (253, 2)
        assert deserialize_varint(b('fdfe00'), 0) == (254, 2)
        assert deserialize_varint(b('fdff00'), 0) == (255, 2)
        assert deserialize_varint(b('fd0001'), 0) == (256, 2)
        assert deserialize_varint(b('fdffff'), 0) == (65535, 2)
        assert deserialize_varint(b('fe00000100'), 0) == (65536, 4)
        assert deserialize_varint(b('feffffffff'), 0) == (4294967295, 4)
        assert deserialize_varint(b('ff0000000001000000'), 0) == (4294967296, 8)
        assert deserialize_varint(b('ffffffffffffffffff'), 0) == (0xffffffffffffffff, 8)
        
        assert deserialize_varint(b('00cc'), 0) == (0, 1)
        assert deserialize_varint(b('01cc'), 0) == (1, 1)
        assert deserialize_varint(b('fbcc'), 0) == (251, 1)
        assert deserialize_varint(b('fccc'), 0) == (252, 1)
        assert deserialize_varint(b('fdfd00cc'), 0) == (253, 2)
        assert deserialize_varint(b('fdfe00cc'), 0) == (254, 2)
        assert deserialize_varint(b('fdff00cc'), 0) == (255, 2)
        assert deserialize_varint(b('fd0001cc'), 0) == (256, 2)
        assert deserialize_varint(b('fdffffcc'), 0) == (65535, 2)
        assert deserialize_varint(b('fe00000100cc'), 0) == (65536, 4)
        assert deserialize_varint(b('feffffffffcc'), 0) == (4294967295, 4)
        assert deserialize_varint(b('ff0000000001000000cc'), 0) == (4294967296, 8)
        assert deserialize_varint(b('ffffffffffffffffffcc'), 0) == (0xffffffffffffffff, 8)

        assert deserialize_varint(b('cc00'), 1) == (0, 1)
        assert deserialize_varint(b('cc01'), 1) == (1, 1)
        assert deserialize_varint(b('ccfb'), 1) == (251, 1)
        assert deserialize_varint(b('ccfc'), 1) == (252, 1)
        assert deserialize_varint(b('ccfdfd00'), 1) == (253, 2)
        assert deserialize_varint(b('ccfdfe00'), 1) == (254, 2)
        assert deserialize_varint(b('ccfdff00'), 1) == (255, 2)
        assert deserialize_varint(b('ccfd0001'), 1) == (256, 2)
        assert deserialize_varint(b('ccfdffff'), 1) == (65535, 2)
        assert deserialize_varint(b('ccfe00000100'), 1) == (65536, 4)
        assert deserialize_varint(b('ccfeffffffff'), 1) == (4294967295, 4)
        assert deserialize_varint(b('ccff0000000001000000'), 1) == (4294967296, 8)
        assert deserialize_varint(b('ccffffffffffffffffff'), 1) == (0xffffffffffffffff, 8)
        
        assert deserialize_varint(b('cc00cc'), 1) == (0, 1)
        assert deserialize_varint(b('cc01cc'), 1) == (1, 1)
        assert deserialize_varint(b('ccfbcc'), 1) == (251, 1)
        assert deserialize_varint(b('ccfccc'), 1) == (252, 1)
        assert deserialize_varint(b('ccfdfd00cc'), 1) == (253, 2)
        assert deserialize_varint(b('ccfdfe00cc'), 1) == (254, 2)
        assert deserialize_varint(b('ccfdff00cc'), 1) == (255, 2)
        assert deserialize_varint(b('ccfd0001cc'), 1) == (256, 2)
        assert deserialize_varint(b('ccfdffffcc'), 1) == (65535, 2)
        assert deserialize_varint(b('ccfe00000100cc'), 1) == (65536, 4)
        assert deserialize_varint(b('ccfeffffffffcc'), 1) == (4294967295, 4)
        assert deserialize_varint(b('ccff0000000001000000cc'), 1) == (4294967296, 8)
        assert deserialize_varint(b('ccffffffffffffffffffcc'), 1) == (0xffffffffffffffff, 8)

        with self.assertRaises(AssertionError, msg='should be raised because `i` argument is negative'):
            deserialize_varint(b('00'), -1)
        with self.assertRaises(AssertionError, msg='should be raised because `data` argument is 0 bytes long'):
            deserialize_varint(b(''))
        with self.assertRaises(AssertionError, msg='should be raised because `data` argument prepended with `fd` but length is 2 instead of 3'):
            deserialize_varint(b('fdff'))
        with self.assertRaises(AssertionError, msg='should be raised because `data` argument prepended with `fe` but length is 4 instead of 5'):
            deserialize_varint(b('feffffff'))
        with self.assertRaises(AssertionError, msg='should be raised because `data` argument prepended with `ff` but length is 8 instead of 9'):
            deserialize_varint(b('ffffffffffffffff'))
        with self.assertRaises(AssertionError, msg='should be raised because `i` argument is 0 when it should be 1 thus a different value is deserialized'):
            assert deserialize_varint(b('cc00'), 0) == (0, 1)
        with self.assertRaises(AssertionError, msg='should be raised because `i` argument is 2 when it should be 1 thus is out of bounds'):
            assert deserialize_varint(b('cc00'), 2) == (0, 1)
        with self.assertRaises(AssertionError, msg='should be raised because `data` argument is of the wrong type'):
            deserialize_varint('wrong type')
        with self.assertRaises(TypeError, msg='should be raised because all arguments are missing'):
            deserialize_varint()