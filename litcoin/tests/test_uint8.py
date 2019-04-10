#!/usr/bin/env python3

from litcoin.binhex import b, x
from litcoin.uint8 import UINT8_SIZE_IN_BYTES, validate_uint8, serialize_uint8, deserialize_uint8
import unittest


class TestUInt8(unittest.TestCase):
    def test_UINT8_SIZE_IN_BYTES(self):
        assert UINT8_SIZE_IN_BYTES == 1

    def test_validate_uint8(self):
        validate_uint8(0)
        validate_uint8(0xff)
        
        with self.assertRaises(AssertionError, msg='should be raised because `n` argument is negative'):
            validate_uint8(-1)
        with self.assertRaises(AssertionError, msg='should be raised because `n` argument is too big for 8 bits'):
            validate_uint8(0x100)
        with self.assertRaises(AssertionError, msg='should be raised because `n` argument is float'):
            validate_uint8(0.0)
        with self.assertRaises(AssertionError, msg='should be raised because `n` argument is the wrong type'):
            validate_uint8('wrong type')
        with self.assertRaises(TypeError, msg='should be raised because all arguments are missing'):
            validate_uint8()

    def test_serialize_uint8(self):
        assert serialize_uint8(0) == b('00')
        assert serialize_uint8(1) == b('01')
        assert serialize_uint8(0xff) == b('ff')
        assert serialize_uint8(0xfe) == b('fe')

        with self.assertRaises(AssertionError, msg='should be raised because `n` argument is negative'):
            serialize_uint8(-1)
        with self.assertRaises(AssertionError, msg='should be raised because `n` argument overflows to more than 8 bits'):
            serialize_uint8(0x100)
        with self.assertRaises(AssertionError, msg='should be raised because `n` argument is of the wrong type'):
            serialize_uint8('wrong type')
        with self.assertRaises(TypeError, msg='should be raised because all arguments are missing'):
            serialize_uint8()

    def test_deserialize_uint8(self):
        assert deserialize_uint8(b('00')) == (0, 1)
        assert deserialize_uint8(b('01')) == (1, 1)
        assert deserialize_uint8(b('ff')) == (0xff, 1)
        assert deserialize_uint8(b('fe')) == (0xfe, 1)
        
        assert deserialize_uint8(b('00'), 0) == (0, 1)
        assert deserialize_uint8(b('01'), 0) == (1, 1)
        assert deserialize_uint8(b('ff'), 0) == (0xff, 1)
        assert deserialize_uint8(b('fe'), 0) == (0xfe, 1)

        assert deserialize_uint8(b('00cc'), 0) == (0, 1)
        assert deserialize_uint8(b('01cc'), 0) == (1, 1)
        assert deserialize_uint8(b('ffcc'), 0) == (0xff, 1)
        assert deserialize_uint8(b('fecc'), 0) == (0xfe, 1)

        assert deserialize_uint8(b('cc00'), 1) == (0, 2)
        assert deserialize_uint8(b('cc01'), 1) == (1, 2)
        assert deserialize_uint8(b('ccff'), 1) == (0xff, 2)
        assert deserialize_uint8(b('ccfe'), 1) == (0xfe, 2)

        assert deserialize_uint8(b('cc00cc'), 1) == (0, 2)
        assert deserialize_uint8(b('cc01cc'), 1) == (1, 2)
        assert deserialize_uint8(b('ccffcc'), 1) == (255, 2)
        assert deserialize_uint8(b('ccfecc'), 1) == (254, 2)

        with self.assertRaises(AssertionError, msg='should be raised because `i` argument is negative'):
            deserialize_uint8(b('00'), -1)
        with self.assertRaises(AssertionError, msg='should be raised because `data` argument is 8 bytes long'):
            deserialize_uint8(b(''))
        with self.assertRaises(AssertionError, msg='should be raised because `i` argument is 0 when it should be 1 thus a different value is deserialized'):
            assert deserialize_uint8(b('cc00'), 0) == 0
        with self.assertRaises(AssertionError, msg='should be raised because `i` argument is 2 when it should be 1 thus there\'s an overflow'):
            deserialize_uint8(b('cc00'), 2)
        with self.assertRaises(AssertionError, msg='should be raised because `data` argument is of the wrong type'):
            deserialize_uint8('wrong type')
        with self.assertRaises(TypeError, msg='should be raised because all arguments are missing'):
            deserialize_uint8()
