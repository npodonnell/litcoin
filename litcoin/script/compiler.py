#!/usr/bin/env python3

from ..binhex import b
from ..uint8 import serialize_uint8, deserialize_uint8
from ..uint16 import serialize_uint16
from ..uint32 import serialize_uint32
from .operations import ScriptOp, OP_0, OP_PUSHDATA1, OP_PUSHDATA2, OP_PUSHDATA4, \
    OP_1NEGATE, OP_1, OP_2, OP_3, OP_4, OP_5, OP_6, OP_7, OP_8, \
    OP_9, OP_10, OP_11, OP_12, OP_13, OP_14, OP_15, OP_16

def compile_bytes(item):
    compiled = b''
    if len(item) == 0:
        # Empty array of bytes - compiles to '00'
        compiled += OP_0.opcode
    else:
        if len(item) < 0x4c:
            # Array of length [1, 75] bytes
            # Compiles to <number of bytes> followed by the bytes themselves
            compiled += serialize_uint8(len(item))
        elif len(item) < 0x100:
            # Array of length [76, 255] bytes
            # Compiles to <0x4c> followed by <number of bytes (1 byte)> followed by the bytes themselves
            compiled += OP_PUSHDATA1.opcode
            compiled += serialize_uint8(len(item))
        elif len(item) < 0x10000:
            # Array of length [256, 65535] bytes
            # Compiles to <0x4d> followed by <number of bytes (2 bytes)> followed by the bytes themselves
            compiled += OP_PUSHDATA2.opcode
            compiled += serialize_uint16(len(item))
        elif len(item) < 0x100000000:
            # Array of length [65536, 4294967295] bytes
            # Compiles to <0x4e> followed by <number of bytes (4 bytes)> followed by the bytes themselves
            compiled += OP_PUSHDATA4.opcode
            compiled += serialize_uint32(len(item))
        compiled += item
    return compiled


def compile_script(script):
    assert type(script) == list, '`script` argument should be of type `list`'
    compiled = b''
    for item in script:
        if type(item) == ScriptOp:
            compiled += item.opcode
        elif type(item) == bytes:
            compiled += compile_bytes(item)
        elif type(item) == str:
            # encode as UTF-8
            compiled += compile_bytes(item.encode('utf-8'))
        elif type(item) == int:
            if item == -1:
                compiled += OP_1NEGATE.opcode
            if item == 0:
                compiled += OP_0.opcode
            if item == 1:
                compiled += OP_1.opcode
            if item == 2:
                compiled += OP_2.opcode
            if item == 3:
                compiled += OP_3.opcode
            if item == 4:
                compiled += OP_4.opcode
            if item == 5:
                compiled += OP_5.opcode
            if item == 6:
                compiled += OP_6.opcode
            if item == 7:
                compiled += OP_7.opcode
            if item == 8:
                compiled += OP_8.opcode
            if item == 9:
                compiled += OP_9.opcode
            if item == 10:
                compiled += OP_10.opcode
            if item == 11:
                compiled += OP_11.opcode
            if item == 12:
                compiled += OP_12.opcode
            if item == 13:
                compiled += OP_13.opcode
            if item == 14:
                compiled += OP_14.opcode
            if item == 15:
                compiled += OP_15.opcode
            if item == 16:
                compiled += OP_16.opcode
        else:
            raise AssertionError('`script` may only contain items of type `ScriptOp`, `bytes`, `str`')
    return compiled
