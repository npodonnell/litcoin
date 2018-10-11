#!/usr/bin/env python3

from litcoin.outpoint import validate_outpoint, serialize_outpoint
from litcoin.uint32 import validate_uint32, serialize_uint32
from litcoin.varint import serialize_varint
from litcoin.script.validation import validate_script
from litcoin.script.serialization import serialize_script


def make_txinput(outpoint, sequence_no, unlockling_script):
    validate_outpoint(outpoint)
    validate_uint32(sequence_no)
    validate_script(unlocking_script)

    return {
        'outpoint': outpoint,
        'sequence_no': sequence_no,
        'unlocking_script': unlocking_script
    }


def validate_txinput(txinput):
    assert type(txinput) == dict, 'type of txinput should be dict'
    assert set(txinput.keys()) == {'outpoint', 'sequence_no', 'unlocking_script'}, 'txinput should have only `outpoint`, `sequence_no` and `unlocking_script` keys'
    validate_outpoint(txinput['outpoint'])
    validate_uint32(txinput['sequence_no'])
    validate_script(txinput['unlocking_script'])


def serialize_txinput(txinput):
    validate_txinput(txinput)
    return serialize_outpoint(txinput['outpoint']) + 
        serialize_varint(len(txinput['unlocking_script'])) +
        serialize_script(txinput['unlocking_script']) +
        serialize_uint32(txinput['sequence_no'])


def deserialize_txinput(data, i=0):
    pass