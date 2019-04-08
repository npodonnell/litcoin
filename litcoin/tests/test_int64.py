#!/usr/bin/env python3

from litcoin.binhex import b, x
from litcoin.int64 import INT64_SIZE_IN_BYTES, validate_int64, serialize_int64, deserialize_int64
import unittest


class TestInt64(unittest.TestCase):
    def test_INT64_SIZE_IN_BYTES(self):
        assert INT64_SIZE_IN_BYTES == 8

    def test_validate_int64(self):
        validate_int64(0)
        validate_int64(0x7fffffffffffffff)
        validate_int64(-0x7fffffffffffffff)
        
        with self.assertRaises(AssertionError, msg='should be raised because positive `n` argument overflows to more than 63 bits'):
            validate_int64(0x8000000000000000)
        with self.assertRaises(AssertionError, msg='should be raised because negative `n` argument overflows to more than 63 bits'):
            validate_int64(-0x8000000000000000)
        with self.assertRaises(AssertionError, msg='should be raised because `n` argument is float'):
            validate_int64(0.0)
        with self.assertRaises(AssertionError, msg='should be raised because `n` argument is the wrong type'):
            validate_int64('wrong type')
        with self.assertRaises(TypeError, msg='should be raised because all arguments are missing'):
            validate_int64()

    def test_serialize_int64(self):
        assert serialize_int64(0) == b('0000000000000000')
        assert serialize_int64(1) == b('0100000000000000')
        assert serialize_int64(-1) == b('ffffffffffffffff')
        assert serialize_int64(-2) == b('feffffffffffffff')

        with self.assertRaises(AssertionError, msg='should be raised because positive `n` argument overflows to more than 63 bits'):
            serialize_int64(0x8000000000000000)
        with self.assertRaises(AssertionError, msg='should be raised because negative `n` argument overflows to more than 63 bits'):
            serialize_int64(-0x8000000000000000)
        with self.assertRaises(AssertionError, msg='should be raised because `n` argument is of the wrong type'):
            serialize_int64('wrong type')
        with self.assertRaises(TypeError, msg='should be raised because all arguments are missing'):
            serialize_int64()

    def test_deserialize_int64(self):
        assert deserialize_int64(b('0000000000000000')) == 0
        assert deserialize_int64(b('0100000000000000')) == 1
        assert deserialize_int64(b('ffffffffffffffff')) == -1
        assert deserialize_int64(b('feffffffffffffff')) == -2

        assert deserialize_int64(b('0000000000000000'), 0) == 0
        assert deserialize_int64(b('0100000000000000'), 0) == 1
        assert deserialize_int64(b('ffffffffffffffff'), 0) == -1
        assert deserialize_int64(b('feffffffffffffff'), 0) == -2

        assert deserialize_int64(b('0000000000000000cc'), 0) == 0
        assert deserialize_int64(b('0100000000000000cc'), 0) == 1
        assert deserialize_int64(b('ffffffffffffffffcc'), 0) == -1
        assert deserialize_int64(b('feffffffffffffffcc'), 0) == -2

        assert deserialize_int64(b('cc0000000000000000'), 1) == 0
        assert deserialize_int64(b('cc0100000000000000'), 1) == 1
        assert deserialize_int64(b('ccffffffffffffffff'), 1) == -1
        assert deserialize_int64(b('ccfeffffffffffffff'), 1) == -2
        
        assert deserialize_int64(b('cc0000000000000000cc'), 1) == 0
        assert deserialize_int64(b('cc0100000000000000cc'), 1) == 1
        assert deserialize_int64(b('ccffffffffffffffffcc'), 1) == -1
        assert deserialize_int64(b('ccfeffffffffffffffcc'), 1) == -2

        with self.assertRaises(AssertionError, msg='should be raised because `data` argument is 7 bytes long'):
            deserialize_int64(b('00000000000000'))
        with self.assertRaises(AssertionError, msg='should be raised because `i` argument is 0 when it should be 1 thus a different value is deserialized'):
            assert deserialize_int64(b('cc0000000000000000'), 0) == 0
        with self.assertRaises(AssertionError, msg='should be raised because `i` argument is 2 when it should be 1 thus there\'s an overflow'):
            deserialize_int64(b('cc0000000000000000'), 2)
        with self.assertRaises(AssertionError, msg='should be raised because `data` argument is of the wrong type'):
            deserialize_int64('wrong type')
        with self.assertRaises(TypeError, msg='should be raised because all arguments are missing'):
            deserialize_int64()
