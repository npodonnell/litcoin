#!/usr/bin/env python3


from litcoin.script.opcodes import *

def serialize_opcode(opcode):
    return opcode.to_bytes(1, byteorder='little', signed=False)


def serialize_uint(n, len):
    return n.to_bytes(len, byteorder='little', signed=False)


def get_le_uint(bytearr, i, size):
    return int.from_bytes(bytearr[i:i + size], byteorder='little', signed=False)


def serialize_script(script):
    assert type(script) == list
    bin_script = b''

    if len(script) == 0:
        return bin_script
    
    i = 0
    while True:
        opcode = script[i]
        bin_script += serialize_opcode(opcode)
        i += 1

        if opcode <= OP_PUSHDATA4:
            if opcode < OP_PUSHDATA1:
                assert i < len(script)
                size = opcode
            else:
                size = script[i]
                i += 1

                assert i < len(script)
                assert type(size) == int
                assert 0 <= size # TODO - check if this is OK
                
                if opcode == OP_PUSHDATA1:
                    assert size <= 0xff
                    sizelen = 1
                elif opcode == OP_PUSHDATA2:
                    assert size <= 0xffff
                    sizelen = 2
                elif opcode == OP_PUSHDATA4:
                    assert size <= 0xffffffff
                    sizelen = 4
                else:
                    assert False
                
                bin_script += serialize_uint(size, sizelen)
                
            # make sure push opcode is followed by
            # bytearray of correct type and length.
            assert type(script[i]) == bytes
            assert len(script[i]) == size
            
            bin_script += script[i]

def deserialize_script(bin_script):
    pass
