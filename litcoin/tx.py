#!/usr/bin/env python3


from .txinput import validate_txinput
from .txoutput import validate_txoutput
from .uint32 import serialize_uint32
from .varint import serialize_varint
from .txinput import serialize_txinput
from .txoutput import serialize_txoutput

"""
These are used whenever bitcoin is undergoing an upgrade. Newer nodes will 
bump up MAX_TX_VERSION first and accept transactions with both the current
version and the new version. Eventually when all (or most) nodes have
upgraded, CURRENT_TX_VERSION will be bumped up to match MAX_TX_VERSION and
older transactions will no longer be accepted.
TODO: This is bitcoin-specific, move these to networks.py
"""
CURRENT_TX_VERSION = 2
MAX_TX_VERSION = 2


def make_tx():
    """
    Returns a 'blank' transaction.
    """
    return {
        'version': CURRENT_TX_VERSION,
        'lock_time': 0,
        'inputs': [],
        'outputs': []
    }


def set_tx_lock_time(tx, lock_time):
    assert type(lock_time) == int
    assert 0 <= lock_time
    assert lock_time <= 0xffffffff
    tx['lock_time'] = lock_time


def add_input(tx, txinput):
    validate_txinput(txinput)
    tx["inputs"].append(txinput)


def add_output(tx, txoutput):
    validate_txoutput(txoutput)
    tx["outputs"].append(txoutput)


def serialize_tx(tx):
    serialized = serialize_uint32(tx["version"])
    # TODO - Check for witness flag
    serialized += serialize_varint(len(tx['inputs']))
    for txinput in tx['inputs']:
        serialized += serialize_txinput(txinput)
    serialized += serialize_varint(len(tx['outputs']))
    for txoutput in tx['outputs']:
        serialized += serialize_txoutput(txoutput)
    # TODO - Check for witness data
    serialized += serialize_uint32(tx["lock_time"])
    return serialized



def deserialize_tx(tx_bytes):
    pass
