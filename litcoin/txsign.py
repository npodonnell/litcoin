#!/usr/bin/env python3

from .txsighash import SIGVERSION_BASE, make_tx_sighash
from .script.compiler import compile_script
from .ec import sign_message
from .binhex import x


def sign_input(tx, input_index, sighash_type, privkey):
    input = tx["inputs"][input_index]
    amount = sum([o["value"] for o in tx["outputs"]])
    print("Amount={0}".format(amount))
    sighash = make_tx_sighash(input["unlocking_script"], tx, input_index, sighash_type, amount, SIGVERSION_BASE)
    print("Sighash={0}".format(x(sighash)))
    signature = sign_message(sighash, privkey)
    print("Signature={0}".format(x(signature)))
    input["unlocking_script"] = compile_script([signature]) + input["unlocking_script"]
    print("Unlocking Script={0}".format(x(input["unlocking_script"])))