#!/usr/bin/env python3

from .txid import TXID_SIZE_IN_BYTES, validate_txid, serialize_txid, deserialize_txid
from .uint32 import UINT32_SIZE_IN_BYTES, validate_uint32, serialize_uint32, deserialize_uint32
from .serialization import validate_data

OUTPOINT_SIZE_IN_BYTES = TXID_SIZE_IN_BYTES + UINT32_SIZE_IN_BYTES


def make_outpoint(txid, output_index):
    validate_txid(txid)
    validate_uint32(output_index)

    return {
        'txid': txid,
        'output_index': output_index
    }


def validate_outpoint(outpoint):
    assert type(outpoint) == dict, 'type of outpoint should be dict'
    assert set(outpoint.keys()) == {'txid', 'output_index'}, 'outpoint should have only `txid` and `output_index` keys'
    validate_txid(outpoint['txid'])
    validate_uint32(outpoint['output_index'])


def serialize_outpoint(outpoint):
    validate_outpoint(outpoint)
    return serialize_txid(outpoint['txid']) + serialize_uint32(outpoint['output_index'])


def deserialize_outpoint(data, i=0):
    validate_data(data, i, OUTPOINT_SIZE_IN_BYTES)
    return make_outpoint(deserialize_txid(data, i), deserialize_uint32(data, i + TXID_SIZE_IN_BYTES))
