#!/usr/bin/env python3

"""
These are used whenever bitcoin is undergoing an upgrade. Newer nodes will 
bump up MAX_TX_VERSION first and accept transactions with both the current
version and the new version. Eventually when all (or most) nodes have
upgraded, CURRENT_TX_VERSION will be bumped up to match MAX_TX_VERSION and
older transactions will no longer be accepted.
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


def serialize_tx(tx):
    pass


def deserialize_tx(tx_bytes):
    pass