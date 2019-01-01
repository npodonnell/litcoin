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
                compiled += OP_0.opcode
            elif len(item) == 1:
                item_uint8 = deserialize_uint8(item)
                if item_uint8 < 0x11:
                    # 80 is the difference between OP_1's opcode (0x51) and 1
                    compiled += serialize_uint8(item_uint8 + 80)
                else:
                    # For 17 or larger we must include a PUSHDATA(1)
                    compiled += b('01')
                    compiled += item
            else:
                if len(item) < 0x4c:
                    compiled += serialize_uint8(len(item))
                elif len(item) < 0x100:
                    compiled += OP_PUSHDATA1.opcode
                    compiled += serialize_uint8(len(item))
                elif len(item) < 0x10000:
                    compiled += OP_PUSHDATA2.opcode
                    compiled += serialize_uint16(len(item))
                elif len(item) < 0x100000000:
                    compiled += OP_PUSHDATA4.opcode
                    compiled += serialize_uint32(len(item))
                compiled += item
        else:
            raise AssertionError('`script` may only contain `ScriptOp` and `bytes` items')
    return compiled
