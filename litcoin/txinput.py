#!/usr/bin/env python3

from litcoin.outpoint import OUTPOINT_SIZE_IN_BYTES, validate_outpoint, serialize_outpoint, deserialize_outpoint
from litcoin.uint32 import UINT32_SIZE_IN_BYTES, validate_uint32, serialize_uint32, deserialize_uint32
from litcoin.varint import VARINT_SIZE_RANGE_IN_BYTES, serialize_varint, deserialize_varint
from litcoin.script.validator import validate_script
from litcoin.script.serialization import serialize_script
from litcoin.serialization import validate_data

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
        serialize_varint(len(txinput['unlocking_script'])) + \
        serialize_script(txinput['unlocking_script']) + \
        serialize_uint32(txinput['sequence_no'])


def deserialize_txinput(data, i=0):
    validate_data(data, i, TXINPUT_SIZE_RANGE_IN_BYTES[0])

    # deserialize outpoint
    outpoint = deserialize_outpoint(data, i)
    i += OUTPOINT_SIZE_IN_BYTES

    # deserialize unlocking script
    (unlocking_script_length, unlocking_script_length_length) = deserialize_varint(data, i)
    i += unlocking_script_length_length
    assert i + unlocking_script_length + UINT32_SIZE_IN_BYTES <= len(data)
    unlocking_script = data[i : i + unlocking_script_length]
    i += unlocking_script_length

    # deserialize sequence number
    sequence_no = deserialize_uint32(data, i)

    return make_txinput(outpoint, unlocking_script, sequence_no)
