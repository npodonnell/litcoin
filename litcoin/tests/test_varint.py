#!/usr/bin/env python3

import unittest
from litcoin.varint import serialize_varint, deserialize_varint


class TestVarInt(unittest.TestCase):
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
        assert serialize_varint(18446744073709551615) == b'\xff\xff\xff\xff\xff\xff\xff\xff\xff'

        with self.assertRaises(AssertionError):
            serialize_varint(-1)
        with self.assertRaises(AssertionError):
            serialize_varint(18446744073709551616)
        

        with self.assertRaises(AssertionError):
            serialize_varint('string')

    def test_deserialize_varint(self):
        assert deserialize_varint(b'\x00', 0) == (0, 1)
        assert deserialize_varint(b'\x01', 0) == (1, 1)
        assert deserialize_varint(b'\xfb', 0) == (251, 1)
        assert deserialize_varint(b'\xfc', 0) == (252, 1)
        assert deserialize_varint(b'\xfd\xfd\x00', 0) == (253, 2)
        assert deserialize_varint(b'\xfd\xfe\x00', 0) == (254, 2)
        assert deserialize_varint(b'\xfd\xff\x00', 0) == (255, 2)
        assert deserialize_varint(b'\xfd\x00\x01', 0) == (256, 2)
        assert deserialize_varint(b'\xfd\xff\xff', 0) == (65535, 2)
        assert deserialize_varint(b'\xfe\x00\x00\x01\x00', 0) == (65536, 4)
        assert deserialize_varint(b'\xfe\xff\xff\xff\xff', 0) == (4294967295, 4)
        assert deserialize_varint(b'\xff\x00\x00\x00\x00\x01\x00\x00\x00', 0) == (4294967296, 8)
        assert deserialize_varint(b'\xff\xff\xff\xff\xff\xff\xff\xff\xff', 0) == (18446744073709551615, 8)
        
        assert deserialize_varint(b'\x42\x00', 1) == (0, 1)
        assert deserialize_varint(b'\x42\x01', 1) == (1, 1)
        assert deserialize_varint(b'\x42\xfb', 1) == (251, 1)
        assert deserialize_varint(b'\x42\xfc', 1) == (252, 1)
        assert deserialize_varint(b'\x42\xfd\xfd\x00', 1) == (253, 2)
        assert deserialize_varint(b'\x42\xfd\xfe\x00', 1) == (254, 2)
        assert deserialize_varint(b'\x42\xfd\xff\x00', 1) == (255, 2)
        assert deserialize_varint(b'\x42\xfd\x00\x01', 1) == (256, 2)
        assert deserialize_varint(b'\x42\xfd\xff\xff', 1) == (65535, 2)
        assert deserialize_varint(b'\x42\xfe\x00\x00\x01\x00', 1) == (65536, 4)
        assert deserialize_varint(b'\x42\xfe\xff\xff\xff\xff', 1) == (4294967295, 4)
        assert deserialize_varint(b'\x42\xff\x00\x00\x00\x00\x01\x00\x00\x00', 1) == (4294967296, 8)
        assert deserialize_varint(b'\x42\xff\xff\xff\xff\xff\xff\xff\xff\xff', 1) == (18446744073709551615, 8)
        
        with self.assertRaises(AssertionError):
            deserialize_varint(b'', 0)
        with self.assertRaises(AssertionError):
            deserialize_varint(b'\xfd\xff', 0)
        with self.assertRaises(AssertionError):
            deserialize_varint(b'\xfe\xff\xff\xff', 0)
        with self.assertRaises(AssertionError):
            deserialize_varint(b'\xff\xff\xff\xff\xff\xff\xff\xff', 0)

        with self.assertRaises(AssertionError):
            deserialize_varint(b'', 1)
        with self.assertRaises(AssertionError):
            deserialize_varint(b'\xfd\xff\xff', 1)
        with self.assertRaises(AssertionError):
            deserialize_varint(b'\xfe\xff\xff\xff\xff', 1)
        with self.assertRaises(AssertionError):
            deserialize_varint(b'\xff\xff\xff\xff\xff\xff\xff\xff\xff', 1)

        with self.assertRaises(AssertionError):
            deserialize_varint('string', 0)
