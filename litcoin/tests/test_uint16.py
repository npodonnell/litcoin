#!/usr/bin/env python3

import unittest
from litcoin.binhex import b, x
from litcoin.uint16 import UINT16_SIZE_IN_BYTES, validate_uint16, serialize_uint16, deserialize_uint16


class TestUInt16(unittest.TestCase):
    def test_UINT16_SIZE_IN_BYTES(self):
        assert UINT16_SIZE_IN_BYTES == 2

    def test_validate_uint16(self):
        validate_uint16(0)
        validate_uint16(0xffff)
        
        with self.assertRaises(AssertionError, msg='should be raised because `n` argument is negative'):
            validate_uint16(-1)
        with self.assertRaises(AssertionError, msg='should be raised because `n` argument is too big for 16 bits'):
            validate_uint16(0x10000)
        with self.assertRaises(AssertionError, msg='should be raised because `n` argument is float'):
            validate_uint16(0.0)
        with self.assertRaises(AssertionError, msg='should be raised because `n` argument is the wrong type'):
            validate_uint16('0')
        with self.assertRaises(TypeError, msg='should be raised because all arguments are missing'):
            validate_uint16()

    def test_serialize_uint16(self):
        assert serialize_uint16(0) == b('0000')
        assert serialize_uint16(1) == b('0100')
        assert serialize_uint16(0xffff) == b('ffff')
        assert serialize_uint16(0xfffe) == b('feff')

        with self.assertRaises(AssertionError, msg='should be raised because `n` argument is negative'):
            serialize_uint16(-1)
        with self.assertRaises(AssertionError, msg='should be raised because `n` argument overflows to more than 16 bits'):
            serialize_uint16(0x10000)
        with self.assertRaises(AssertionError, msg='should be raised because `n` argument is of the wrong type'):
            serialize_uint16('wrong type')
        with self.assertRaises(TypeError, msg='should be raised because all arguments are missing'):
            serialize_uint16()

    def test_deserialize_uint16(self):
        assert deserialize_uint16(b('0000')) == 0
        assert deserialize_uint16(b('0100')) == 1
        assert deserialize_uint16(b('ffff')) == 0xffff
        assert deserialize_uint16(b('feff')) == 0xfffe

        assert deserialize_uint16(b('0000'), 0) == 0
        assert deserialize_uint16(b('0100'), 0) == 1
        assert deserialize_uint16(b('ffff'), 0) == 0xffff
        assert deserialize_uint16(b('feff'), 0) == 0xfffe

        assert deserialize_uint16(b('0000cc'), 0) == 0
        assert deserialize_uint16(b('0100cc'), 0) == 1
        assert deserialize_uint16(b('ffffcc'), 0) == 0xffff
        assert deserialize_uint16(b('feffcc'), 0) == 0xfffe

        assert deserialize_uint16(b('cc0000'), 1) == 0
        assert deserialize_uint16(b('cc0100'), 1) == 1
        assert deserialize_uint16(b('ccffff'), 1) == 0xffff
        assert deserialize_uint16(b('ccfeff'), 1) == 0xfffe
        
        assert deserialize_uint16(b('cc0000cc'), 1) == 0
        assert deserialize_uint16(b('cc0100cc'), 1) == 1
        assert deserialize_uint16(b('ccffffcc'), 1) == 0xffff
        assert deserialize_uint16(b('ccfeffcc'), 1) == 0xfffe

        with self.assertRaises(AssertionError, msg='should be raised because `i` argument is negative'):
            deserialize_uint16(b('0000'), -1)
        with self.assertRaises(AssertionError, msg='should be raised because `data` argument is 1 byte long'):
            deserialize_uint16(b('00'))
        with self.assertRaises(AssertionError, msg='should be raised because `i` argument is 0 when it should be 1 thus a different value is deserialized'):
            assert deserialize_uint16(b('cc0000'), 0) == 0
        with self.assertRaises(AssertionError, msg='should be raised because `i` argument is 2 when it should be 1 thus there\'s an overflow'):
            deserialize_uint16(b('cc0000'), 2)
        with self.assertRaises(AssertionError, msg='should be raised because `data` argument is of the wrong type'):
            deserialize_uint16('wrong type')
        with self.assertRaises(TypeError, msg='should be raised because all arguments are missing'):
            deserialize_uint16()
