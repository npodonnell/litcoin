#!/usr/bin/env python3

import unittest
from litcoin.binhex import b, x
from litcoin.uint32 import UINT32_SIZE_IN_BYTES, validate_uint32, serialize_uint32, deserialize_uint32


class TestUInt32(unittest.TestCase):
    def test_UINT32_SIZE_IN_BYTES(self):
        assert UINT32_SIZE_IN_BYTES == 4

    def test_validate_uint32(self):
        validate_uint32(0)
        validate_uint32(0xffffffff)
        
        with self.assertRaises(AssertionError, msg='should be raised because `n` argument is negative'):
            validate_uint32(-1)
        with self.assertRaises(AssertionError, msg='should be raised because `n` argument is too big for 32 bits'):
            validate_uint32(0x100000000)
        with self.assertRaises(AssertionError, msg='should be raised because `n` argument is float'):
            validate_uint32(0.0)
        with self.assertRaises(AssertionError, msg='should be raised because `n` argument is the wrong type'):
            validate_uint32('wrong type')
        with self.assertRaises(TypeError, msg='should be raised because all arguments are missing'):
            validate_uint32()

    def test_serialize_uint32(self):
        assert serialize_uint32(0) == b('00000000')
        assert serialize_uint32(1) == b('01000000')
        assert serialize_uint32(0xffffffff) == b('ffffffff')
        assert serialize_uint32(0xfffffffe) == b('feffffff')

        with self.assertRaises(AssertionError, msg='should be raised because `n` argument is negative'):
            serialize_uint32(-1)
        with self.assertRaises(AssertionError, msg='should be raised because `n` argument overflows to more than 32 bits'):
            serialize_uint32(0x100000000)
        with self.assertRaises(AssertionError, msg='should be raised because `n` argument is of the wrong type'):
            serialize_uint32('wrong type')
        with self.assertRaises(TypeError, msg='should be raised because all arguments are missing'):
            serialize_uint32()

    def test_deserialize_uint32(self):
        assert deserialize_uint32(b('00000000')) == 0
        assert deserialize_uint32(b('01000000')) == 1
        assert deserialize_uint32(b('ffffffff')) == 0xffffffff
        assert deserialize_uint32(b('feffffff')) == 0xfffffffe

        assert deserialize_uint32(b('00000000'), 0) == 0
        assert deserialize_uint32(b('01000000'), 0) == 1
        assert deserialize_uint32(b('ffffffff'), 0) == 0xffffffff
        assert deserialize_uint32(b('feffffff'), 0) == 0xfffffffe

        assert deserialize_uint32(b('00000000cc'), 0) == 0
        assert deserialize_uint32(b('01000000cc'), 0) == 1
        assert deserialize_uint32(b('ffffffffcc'), 0) == 0xffffffff
        assert deserialize_uint32(b('feffffffcc'), 0) == 0xfffffffe

        assert deserialize_uint32(b('cc00000000'), 1) == 0
        assert deserialize_uint32(b('cc01000000'), 1) == 1
        assert deserialize_uint32(b('ccffffffff'), 1) == 0xffffffff
        assert deserialize_uint32(b('ccfeffffff'), 1) == 0xfffffffe
        
        assert deserialize_uint32(b('cc00000000cc'), 1) == 0
        assert deserialize_uint32(b('cc01000000cc'), 1) == 1
        assert deserialize_uint32(b('ccffffffffcc'), 1) == 0xffffffff
        assert deserialize_uint32(b('ccfeffffffcc'), 1) == 0xfffffffe

        with self.assertRaises(AssertionError, msg='should be raised because `i` argument is negative'):
            deserialize_uint32(b('00000000'), -1)
        with self.assertRaises(AssertionError, msg='should be raised because `data` argument is 3 bytes long'):
            deserialize_uint32(b('000000'))
        with self.assertRaises(AssertionError, msg='should be raised because `i` argument is 0 when it should be 1 thus a different value is deserialized'):
            assert deserialize_uint32(b('cc00000000'), 0) == 0
        with self.assertRaises(AssertionError, msg='should be raised because `i` argument is 2 when it should be 1 thus there\'s an overflow'):
            deserialize_uint32(b('cc00000000'), 2)
        with self.assertRaises(AssertionError, msg='should be raised because `data` argument is of the wrong type'):
            deserialize_uint32('wrong type')
        with self.assertRaises(TypeError, msg='should be raised because all arguments are missing'):
            deserialize_uint32()
