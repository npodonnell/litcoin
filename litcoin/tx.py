#!/usr/bin/env python3


CURRENT_TX_VERSION = 2
MAX_TX_VERSION = 2


def make_tx():
    """
    Makes a "blank" transaction
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