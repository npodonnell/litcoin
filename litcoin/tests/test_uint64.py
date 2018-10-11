#!/usr/bin/env python3

import unittest
from litcoin.binhex import b, x
from litcoin.uint64 import validate_uint64, serialize_uint64, deserialize_uint64


class TestUInt64(unittest.TestCase):
    def test_validate_uint64(self):
        validate_uint64(0)
        validate_uint64(0xffffffffffffffff)
        
        with self.assertRaises(AssertionError, msg='should be raised because `n` argument is negative'):
            validate_uint64(-1)
        with self.assertRaises(AssertionError, msg='should be raised because `n` argument is too big for 64 bits'):
            validate_uint64(0x10000000000000000)
        with self.assertRaises(AssertionError, msg='should be raised because `n` argument is float'):
            validate_uint64(0.0)
        with self.assertRaises(AssertionError, msg='should be raised because `n` argument is the wrong type'):
            validate_uint64('0')
        with self.assertRaises(TypeError, msg='should be raised because all arguments are missing'):
            validate_uint64()

    def test_serialize_uint64(self):
        assert serialize_uint64(0) == b('0000000000000000')
        assert serialize_uint64(1) == b('0100000000000000')
        assert serialize_uint64(0xffffffffffffffff) == b('ffffffffffffffff')
        assert serialize_uint64(0xfffffffffffffffe) == b('feffffffffffffff')

        with self.assertRaises(AssertionError, msg='should be raised because `n` argument is negative'):
            serialize_uint64(-1)
        with self.assertRaises(AssertionError, msg='should be raised because `n` argument overflows to more than 64 bits'):
            serialize_uint64(0x10000000000000000)
        with self.assertRaises(AssertionError, msg='should be raised because `n` argument is of the wrong type'):
            serialize_uint64('wrong type')
        with self.assertRaises(TypeError, msg='should be raised because all arguments are missing'):
            serialize_uint64()

    def test_deserialize_uint64(self):
        assert deserialize_uint64(b('0000000000000000')) == 0
        assert deserialize_uint64(b('0100000000000000')) == 1
        assert deserialize_uint64(b('ffffffffffffffff')) == 0xffffffffffffffff
        assert deserialize_uint64(b('feffffffffffffff')) == 0xfffffffffffffffe

        assert deserialize_uint64(b('0000000000000000'), 0) == 0
        assert deserialize_uint64(b('0100000000000000'), 0) == 1
        assert deserialize_uint64(b('ffffffffffffffff'), 0) == 0xffffffffffffffff
        assert deserialize_uint64(b('feffffffffffffff'), 0) == 0xfffffffffffffffe

        assert deserialize_uint64(b('0000000000000000cc'), 0) == 0
        assert deserialize_uint64(b('0100000000000000cc'), 0) == 1
        assert deserialize_uint64(b('ffffffffffffffffcc'), 0) == 0xffffffffffffffff
        assert deserialize_uint64(b('feffffffffffffffcc'), 0) == 0xfffffffffffffffe

        assert deserialize_uint64(b('cc0000000000000000'), 1) == 0
        assert deserialize_uint64(b('cc0100000000000000'), 1) == 1
        assert deserialize_uint64(b('ccffffffffffffffff'), 1) == 0xffffffffffffffff
        assert deserialize_uint64(b('ccfeffffffffffffff'), 1) == 0xfffffffffffffffe
        
        assert deserialize_uint64(b('cc0000000000000000cc'), 1) == 0
        assert deserialize_uint64(b('cc0100000000000000cc'), 1) == 1
        assert deserialize_uint64(b('ccffffffffffffffffcc'), 1) == 0xffffffffffffffff
        assert deserialize_uint64(b('ccfeffffffffffffffcc'), 1) == 0xfffffffffffffffe

        with self.assertRaises(AssertionError, msg='should be raised because `i` argument is negative'):
            deserialize_uint64(b('0000000000000000'), -1)
        with self.assertRaises(AssertionError, msg='should be raised because `data` argument is 7 bytes long'):
            deserialize_uint64(b('00000000000000'))
        with self.assertRaises(AssertionError, msg='should be raised because `i` argument is 0 when it should be 1 thus a different value is deserialized'):
            assert deserialize_uint64(b('cc0000000000000000'), 0) == 0
        with self.assertRaises(AssertionError, msg='should be raised because `i` argument is 2 when it should be 1 thus there\'s an overflow'):
            deserialize_uint64(b('cc0000000000000000'), 2)
        with self.assertRaises(AssertionError, msg='should be raised because `data` argument is of the wrong type'):
            deserialize_uint64('wrong type')
        with self.assertRaises(TypeError, msg='should be raised because all arguments are missing'):
            deserialize_uint64()
