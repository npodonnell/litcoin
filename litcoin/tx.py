#!/usr/bin/env python3

from .txinput import validate_txinput
from .txoutput import validate_txoutput
from .int32 import INT32_SIZE_IN_BYTES, validate_int32, deserialize_int32
from .uint32 import UINT32_SIZE_IN_BYTES, validate_uint32, serialize_uint32, deserialize_uint32
from .varint import VARINT_SIZE_RANGE_IN_BYTES, serialize_varint, deserialize_varint
from .txinput import serialize_txinput, deserialize_txinput, txinput_to_human_readable, txinput_copy
from .txoutput import serialize_txoutput, deserialize_txoutput, txoutput_to_human_readable, txoutput_copy
from .serialization import ensure_enough_data

"""
These are used whenever bitcoin is undergoing an upgrade. Newer nodes will 
bump up MAX_TX_VERSION first and accept transactions with both the current
version and the new version. Eventually when all (or most) nodes have
upgraded, CURRENT_TX_VERSION will be bumped up to match MAX_TX_VERSION and
older transactions will no longer be accepted.
TODO: This is bitcoin-specific, move these to networks.py

Code Pointer: src/primitives/transaction.h
"""
MIN_TX_VERSION = 1
CURRENT_TX_VERSION = 2
MAX_TX_VERSION = 2
TX_MIN_SIZE_IN_BYTES = INT32_SIZE_IN_BYTES + VARINT_SIZE_RANGE_IN_BYTES[0] + VARINT_SIZE_RANGE_IN_BYTES[0] + UINT32_SIZE_IN_BYTES


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


def set_tx_version(tx, version):
    validate_int32(version)
    assert MIN_TX_VERSION <= version <= MAX_TX_VERSION, \
        "`version` should be in the range [{0}, {1}]".format(MIN_TX_VERSION, MAX_TX_VERSION)
    tx["version"] = version


def set_tx_lock_time(tx, lock_time):
    validate_uint32(lock_time)
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


def deserialize_tx(data, pos=0):
    ensure_enough_data(data, pos, TX_MIN_SIZE_IN_BYTES)
    tx = make_tx()

    # Deserialize version
    (version, pos) = deserialize_int32(data, pos)
    set_tx_version(tx, version)

    # Deserialize input count
    (n_inputs, pos) = deserialize_varint(data, pos)

    # Deserialize inputs
    for _ in range(n_inputs):
        (txinput, pos) = deserialize_txinput(data, pos)
        add_input(tx, txinput)
        
    # Deserialize output count
    (n_outputs, pos) = deserialize_varint(data, pos)

    # Deserialize outputs
    for _ in range(n_outputs):
        (txoutput, pos) = deserialize_txoutput(data, pos)
        add_output(tx, txoutput)

    # Deserialize lock time
    (lock_time, pos) = deserialize_uint32(data, pos)
    set_tx_lock_time(tx, lock_time)

    return tx, pos
    

def tx_to_human_readable(tx):
    return {
        'version': tx['version'],
        'lock_time': tx['lock_time'],
        'inputs': [txinput_to_human_readable(txinput) for txinput in tx['inputs']],
        'outputs': [txoutput_to_human_readable(txoutput) for txoutput in tx['outputs']]
    }


def tx_copy(tx):
    """
    Performs a deep-copy of a transaction
    """
    return {
        'version': tx["version"],
        'lock_time': tx["lock_time"],
        'inputs': [txinput_copy(i) for i in tx["inputs"]],
        'outputs': [txoutput_copy(i) for i in tx["outputs"]]
    }
