#!/usr/bin/env python3

from ..binhex import b
from ..uint8 import serialize_uint8, deserialize_uint8
from ..uint16 import serialize_uint16
from ..uint32 import serialize_uint32
from .operations import ScriptOp, OP_0, OP_PUSHDATA1, OP_PUSHDATA2, OP_PUSHDATA4

def compile_script(script):
    assert type(script) == list, '`script` argument should be of type `list`'

    compiled = b('')

    for item in script:
        if type(item) == ScriptOp:
            compiled += item.opcode
        elif type(item) == bytes:
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
        else:
            raise AssertionError('`script` may only contain `ScriptOp` and `bytes` items')
    return compiled
