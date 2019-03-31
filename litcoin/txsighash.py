#!/usr/bin/env python3

from .tx import tx_copy
from .script.compiler import compile_script
from .script.operations import OP_CODESEPARATOR
from .binhex import b

# Sighash types
# See script/interpreter.h
SIGHASH_ALL = 1
SIGHASH_NONE = 2
SIGHASH_SINGLE = 3
SIGHASH_ANYONECANPAY = 0x80

HASH_ONE = b('0100000000000000000000000000000000000000000000000000000000000000')


def find_and_delete(script, b):
    """
    TODO
    """
    return script


def make_tx_sighash(script, tx, type, input_index, amount, sig_version, sighash_type):
    """
    Compute signature hash for a transaction input
    Code pointers:
      src/script/interpreter.cpp (new)
      src/test/sighash_tests.cpp (old)
    """
    if len(tx["inputs"]) <= input_index:
        return HASH_ONE

    # copy transaction to temporary copy
    txtemp = tx_copy(tx)

    # clear the unlocking scripts
    for txinput in txtemp["inputs"]:
        txinput["unlocking_script"] = compile_script([])
    

    txtemp["inputs"][input_index]["unlocking_script"] = find_and_delete(script, compile_script([OP_CODESEPERATOR]))

    if (sighash_type & 0x1f) == SIGHASH_NONE:
        txtemp["outputs"] = []
