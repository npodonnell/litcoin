#!/usr/bin/env python3


def make_outpoint(prev_txhash, prev_output_index):
    assert type(prev_txhash) == bytes
    assert type(prev_output_index) == int
    assert len(prev_txhash) == 32
    assert 0 <= prev_output_index

    return {
        'prev_txhash': prev_txhash,
        'prev_output_index': prev_output_index
    }


def serialize_outpoint(outpoint):
    pass