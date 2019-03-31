#!/usr/bin/env python3

from litcoin.binhex import b

# Sighash types
# See script/interpreter.h
SIGHASH_ALL = 1
SIGHASH_NONE = 2
SIGHASH_SINGLE = 3
SIGHASH_ANYONECANPAY = 0x80

HASH_ONE = b('0100000000000000000000000000000000000000000000000000000000000000')

# src/test/sighash_tests.cpp
# 
def make_tx_sighash(script, tx, type, input_index):
    """
    Compute signature hash for a transaction input
    """
    if len(tx["inputs"]) <= input_index:
        return HASH_ONE
