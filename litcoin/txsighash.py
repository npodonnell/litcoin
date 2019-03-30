#!/usr/bin/env python3

from litcoin.binhex import b


HASH_ONE = b('0100000000000000000000000000000000000000000000000000000000000000')


def make_tx_sighash(script, tx, type, input_index):
    """
    Compute signature hash for a transaction input
    """
    pass
