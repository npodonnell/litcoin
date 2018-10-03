#!/usr/bin/env python3

from litcoin.script.opcodes import OP_0, OP_PUSHDATA1, OP_PUSHDATA2, OP_PUSHDATA4
from litcoin.script.constants import MAX_SCRIPT_SIZE


def serialize_opcode(opcode):
    return int.to_bytes(opcode, 1, byteorder='little', signed=False)


def serialize_uint(n, len):
    return int.to_bytes(n, len, byteorder='little', signed=False)


def serialize_script(script):
    assert type(script) == list
    bin_script = b''

    if len(script) == 0:
        return bin_script
    
    i = 0
    while i < len(script):
        assert type(script[i]) == int

        opcode = script[i]
        bin_script += serialize_opcode(opcode)
        i += 1

        if opcode == OP_0:
            continue
        elif opcode < OP_PUSHDATA1:
            assert i < len(script)
            assert type(script[i]) == bytes
            assert len(script[i]) == opcode
            bin_script += script[i]
            i += 1
        elif opcode == OP_PUSHDATA1:
            assert i + 1 < len(script)
            assert type(script[i]) == int
            assert 0x4c <= script[i] and script[i] <= 0xff
            assert type(script[i + 1]) == bytes
            assert len(script[i + 1]) == script[i]
            bin_script += serialize_uint(script[i], 1)
            bin_script += script[i + 1]
            i += 2
        elif opcode == OP_PUSHDATA2:
            assert i + 1 < len(script)
            assert type(script[i]) == int
            assert 0x100 <= script[i] and script[i] <= 0xffff
            assert type(script[i + 1]) == bytes
            assert len(script[i + 1]) == script[i]
            bin_script += serialize_uint(script[i], 2)
            bin_script += script[i + 1]
            i += 2
        elif opcode == OP_PUSHDATA4:
            assert i + 1 < len(script)
            assert type(script[i]) == int
            assert 0x10000 <= script[i] and script[i] <= 0xffffffff
            assert type(script[i + 1]) == bytes
            assert len(script[i + 1]) == script[i]
            bin_script += serialize_uint(script[i], 4)
            bin_script += script[i + 1]
            i += 2
        else:
            continue

    assert len(bin_script) <= MAX_SCRIPT_SIZE
    return bin_script
