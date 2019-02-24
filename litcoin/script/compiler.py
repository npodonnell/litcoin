#!/usr/bin/env python3

from ..binhex import b
from ..uint8 import serialize_uint8, deserialize_uint8
from ..uint16 import serialize_uint16
from ..uint32 import serialize_uint32
from .operations import ScriptOp, OP_0, OP_PUSHDATA1, OP_PUSHDATA2, OP_PUSHDATA4, \
    OP_1NEGATE, OP_1, OP_2, OP_3, OP_4, OP_5, OP_6, OP_7, OP_8, \
    OP_9, OP_10, OP_11, OP_12, OP_13, OP_14, OP_15, OP_16


def bytes_needed(i):
    """
    Compute the number of bytes needed to hold arbitrary-length integer i
    """
    bn = 1
    while True:
        i >>= 7
        if i == 1:
            # negative sign bit
            return bn + 1
        elif i == 0:
            return bn
        i >>= 1
        bn += 1
    return bn


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


def compile_int(item):
    if item == -1:
        return OP_1NEGATE.opcode
    elif item == 0:
        return OP_0.opcode
    elif item == 1:
        return OP_1.opcode
    elif item == 2:
        return OP_2.opcode
    elif item == 3:
        return OP_3.opcode
    elif item == 4:
        return OP_4.opcode
    elif item == 5:
        return OP_5.opcode
    elif item == 6:
        return OP_6.opcode
    elif item == 7:
        return OP_7.opcode
    elif item == 8:
        return OP_8.opcode
    elif item == 9:
        return OP_9.opcode
    elif item == 10:
        return OP_10.opcode
    elif item == 11:
        return OP_11.opcode
    elif item == 12:
        return OP_12.opcode
    elif item == 13:
        return OP_13.opcode
    elif item == 14:
        return OP_14.opcode
    elif item == 15:
        return OP_15.opcode
    elif item == 16:
        return OP_16.opcode
    elif item >= 16:
        return compile_bytes((item).to_bytes(bytes_needed(item), byteorder='little'))

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
            compiled += compile_int(item)
        else:
            raise AssertionError('`script` may only contain items of type `ScriptOp`, `bytes`, `str` or `int`')
    return compiled
