#!/usr/bin/env python3

from litcoin.outpoint import OUTPOINT_SIZE_IN_BYTES, validate_outpoint, serialize_outpoint, \
    deserialize_outpoint, outpoint_to_human_readable, outpoint_copy
from litcoin.uint32 import UINT32_SIZE_IN_BYTES, validate_uint32, serialize_uint32, deserialize_uint32
from litcoin.varint import VARINT_SIZE_RANGE_IN_BYTES
from litcoin.script.validator import validate_script
from litcoin.script.serialization import serialize_script, deserialize_script
from litcoin.script.humanreadable import script_to_human_readable
from litcoin.script.copy import script_copy
from litcoin.serialization import ensure_enough_data

TXINPUT_SIZE_RANGE_IN_BYTES = ( \
    OUTPOINT_SIZE_IN_BYTES + VARINT_SIZE_RANGE_IN_BYTES[0] + UINT32_SIZE_IN_BYTES, \
)


def make_txinput(outpoint, unlocking_script, sequence_no):
    validate_outpoint(outpoint)
    validate_script(unlocking_script)
    validate_uint32(sequence_no)

    return {
        'outpoint': outpoint,
        'unlocking_script': unlocking_script,
        'sequence_no': sequence_no
    }


def validate_txinput(txinput):
    assert type(txinput) == dict, 'type of txinput should be dict'
    assert set(txinput.keys()) == {'outpoint', 'sequence_no', 'unlocking_script'}, \
        'txinput should have only `outpoint`, `sequence_no` and `unlocking_script` keys'
    validate_outpoint(txinput['outpoint'])
    validate_script(txinput['unlocking_script'])
    validate_uint32(txinput['sequence_no'])


def serialize_txinput(txinput):
    validate_txinput(txinput)
    return serialize_outpoint(txinput['outpoint']) + \
        serialize_script(txinput['unlocking_script']) + \
        serialize_uint32(txinput['sequence_no'])


def deserialize_txinput(data, pos=0):
    ensure_enough_data(data, pos, TXINPUT_SIZE_RANGE_IN_BYTES[0])
    (outpoint, pos) = deserialize_outpoint(data, pos)
    (unlocking_script, pos) = deserialize_script(data, pos)
    (sequence_no, pos) = deserialize_uint32(data, pos)
    return (make_txinput(outpoint, unlocking_script, sequence_no), pos)


def txinput_to_human_readable(txinput):
    return {
        'outpoint': outpoint_to_human_readable(txinput['outpoint']),
        'unlocking_script': script_to_human_readable(txinput['unlocking_script']),
        'sequence_no': txinput['sequence_no']
    }


def txinput_copy(txinput):
    """
    Performs a deep-copy of a txinput
    """
    return {
        "outpoint": outpoint_copy(txinput["outpoint"]),
        "unlocking_script": script_copy(txinput["unlocking_script"]),
        "sequence_no": txinput["sequence_no"]
    }
