#!/usr/bin/env python3

from .txsighash import SIGVERSION_BASE, SIGVERSION_WITNESS_V0, make_tx_sighash
from .script.compiler import compile_script
from .ec import sign_message
from .uint8 import serialize_uint8
from .binhex import x, b


def sign_p2sh_input(tx, input_index, sighash_type, privkey):
    input = tx["inputs"][input_index]
    amount = sum([o["value"] for o in tx["outputs"]])
    sighash = make_tx_sighash(input["unlocking_script"], tx, input_index, sighash_type, amount, SIGVERSION_BASE)

    while True:
        signature = sign_message(sighash, privkey)
        # In DER serialization, all values are interpreted as big-endian, signed integers. The highest bit in the integer indicates
        # its signed-ness; 0 is positive, 1 is negative. When the value is interpreted as a negative integer, it must be converted
        # to a positive value by prepending a 0x00 byte so that the highest bit is 0. We can avoid this prepending by ensuring that
        # our highest bit is always 0, and thus we must check that the first byte is less than 0x80.
        if signature[4] < 0x80:
            break
    input["unlocking_script"] = compile_script([signature + serialize_uint8(sighash_type), input["unlocking_script"]])
