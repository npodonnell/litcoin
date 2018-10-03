#!/usr/bin/env python3

import unittest
from litcoin.script.serialization import serialize_opcode, serialize_uint, serialize_script
from litcoin.script.opcodes import OP_0, OP_PUSHDATA1, OP_PUSHDATA2

class TestScriptSerialization(unittest.TestCase):
    def test_serialize_opcode(self):
        assert serialize_opcode(0) == b'\x00'
        assert serialize_opcode(1) == b'\x01'
        assert serialize_opcode(255) == b'\xff'

        with self.assertRaises(OverflowError):
            serialize_opcode(256)

    def test_serialize_uint(self):
        assert serialize_uint(0, 1) == b'\x00'
        assert serialize_uint(255, 1) == b'\xff'
        with self.assertRaises(OverflowError):
            serialize_uint(256, 1)

        assert serialize_uint(256, 2) == b'\x00\x01'
        assert serialize_uint(65535, 2) == b'\xff\xff'
        with self.assertRaises(OverflowError):
            serialize_uint(65536, 2)

        assert serialize_uint(65536, 4) == b'\x00\x00\x01\x00'
        assert serialize_uint(4294967295, 4) == b'\xff\xff\xff\xff'
        with self.assertRaises(OverflowError):
            serialize_uint(4294967296, 4)
    
    def test_serialize_script(self):
        def ba(size):
            """
            Create a dummy byte array of *size* bytes
            """
            return b'\xff' * size
        
        # Valid scripts
        assert serialize_script([]) == b''
        assert serialize_script([OP_0]) == b'\x00'
        assert serialize_script([OP_0, OP_0]) == b'\x00\x00'
        assert serialize_script([OP_0, OP_0, OP_0]) == b'\x00\x00\x00'
        assert serialize_script([1, b'\xff']) == b'\x01\xff'
        assert serialize_script([2, b'\xff\xff']) == b'\x02\xff\xff'
        assert serialize_script([3, b'\xff\xff\xff']) == b'\x03\xff\xff\xff'
        assert serialize_script([75, ba(75)]) == b'\x4b' + ba(75)
        assert serialize_script([OP_PUSHDATA1, 76, ba(76)]) == b'\x4c\x4c' + ba(76)
        assert serialize_script([OP_PUSHDATA1, 255, ba(255)]) == b'\x4c\xff' + ba(255)
        assert serialize_script([OP_PUSHDATA2, 256, ba(256)]) == b'\x4d\x00\x01' + ba(256)

        # Invalid scripts
        

if __name__ == '__main__':
    unittest.main()
