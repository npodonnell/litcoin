#!/usr/bin/env python3

from .uint256 import UINT256_SIZE_IN_BYTES, validate_uint256, serialize_uint256, deserialize_uint256
from .uint32 import UINT32_SIZE_IN_BYTES, validate_uint32, serialize_uint32, deserialize_uint32
from .serialization import ensure_enough_data

OUTPOINT_SIZE_IN_BYTES = UINT256_SIZE_IN_BYTES + UINT32_SIZE_IN_BYTES


def make_outpoint(txid, output_index):
    validate_uint256(txid)
    validate_uint32(output_index)

    return {
        'txid': txid,
        'output_index': output_index
    }


def validate_outpoint(outpoint):
    assert type(outpoint) == dict, 'type of outpoint should be dict'
    assert set(outpoint.keys()) == {'txid', 'output_index'}, 'outpoint should have only `txid` and `output_index` keys'
    validate_uint256(outpoint['txid'])
    validate_uint32(outpoint['output_index'])


def serialize_outpoint(outpoint):
    validate_outpoint(outpoint)
    return serialize_uint256(outpoint['txid']) + serialize_uint32(outpoint['output_index'])


def deserialize_outpoint(data, pos=0):
    ensure_enough_data(data, pos, OUTPOINT_SIZE_IN_BYTES)
    (txid, pos) = deserialize_uint256(data, pos)
    (output_index, pos) = deserialize_uint32(data, pos)
    return (make_outpoint(txid, output_index), pos)


def outpoint_to_human_readable(outpoint):
    return {
        'txid': outpoint['txid'],
        'output_index': outpoint['output_index']
    }


def outpoint_copy(outpoint):
    """
    Performs a deep-copy of an outpoint
    """
    return {
        "txid": outpoint["txid"],
        "output_index": outpoint["output_index"]
    }
