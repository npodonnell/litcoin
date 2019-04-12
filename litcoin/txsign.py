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
        # Keep signing until we have a low "r" value
        signature = sign_message(sighash, privkey)
        if len(signature) < 71:
            break
    input["unlocking_script"] = compile_script([signature + serialize_uint8(sighash_type), input["unlocking_script"]])
