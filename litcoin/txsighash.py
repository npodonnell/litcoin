#!/usr/bin/env python3

from .tx import tx_copy
from .script.compiler import compile_script
from .script.operations import OP_CODESEPARATOR
from .binhex import b, x
from .hashing import double_sha
from .outpoint import serialize_outpoint
from .txoutput import serialize_txoutput
from .uint32 import serialize_uint32
from .uint64 import serialize_uint64

# Sighash types
# See script/interpreter.h
SIGHASH_ALL = 1
SIGHASH_NONE = 2
SIGHASH_SINGLE = 3
SIGHASH_ANYONECANPAY = 0x80

# Sigversions
# See script/interpreter.h
SIGVERSION_BASE = 0
SIGVERSION_WITNESS_V0 = 1

HASH_ONE = b("0100000000000000000000000000000000000000000000000000000000000000")


def get_prevout_hash(tx):
    data = b("")
    for txinput in tx["inputs"]:
        data += serialize_outpoint(txinput["outpoint"])
    return double_sha(data)


def get_sequence_hash(tx):
    data = b("")
    for txinput in tx["inputs"]:
        data += serialize_uint32(txinput["sequence_no"])
    return double_sha(data)


def get_outputs_hash(tx):
    data = b("")
    for txoutput in tx["outputs"]:
        data += serialize_txoutput(txoutput)
    return double_sha(data)


def make_tx_sighash(script, tx, input_index, sighash_type, amount, sigversion):
    assert type(script) is bytes, "`script` should be of type bytes"
    assert input_index < len(tx["inputs"]), "`input_index` should be less than the number of inputs"

    if sigversion == SIGVERSION_WITNESS_V0:
        hash_prevouts = b('0000000000000000000000000000000000000000000000000000000000000000')
        hash_sequence = b('0000000000000000000000000000000000000000000000000000000000000000')
        hash_outputs = b('0000000000000000000000000000000000000000000000000000000000000000')

        if not (sighash_type & SIGHASH_ANYONECANPAY):
            hash_prevouts = get_prevout_hash(tx)

        if not (sighash_type & SIGHASH_ANYONECANPAY) and (sighash_type & 0x1f) != SIGHASH_SINGLE \
            and (sighash_type & 0x1f) != SIGHASH_NONE:
            hash_sequence = get_sequence_hash(tx)
        
        if (sighash_type & 0x1f) != SIGHASH_SINGLE and (sighash_type & 0x1f) != SIGHASH_NONE:
            hash_outputs = get_outputs_hash(tx)
        elif (sighash_type & 0x1f) == SIGHASH_SINGLE and input_index < len(tx["outputs"]):
            hash_outputs = double_sha(serialize_txoutput(tx["outputs"][input_index]))
        
        hash_version = double_sha(serialize_uint32(tx["version"]))
        
        return double_sha(
            serialize_uint32(tx["version"]) +
            hash_prevouts +
            hash_sequence +
            serialize_outpoint(tx["inputs"][input_index]["outpoint"]) +
            script +
            serialize_uint64(amount) +
            serialize_uint32(tx["inputs"][input_index]["sequence_no"]) +
            hash_outputs +
            serialize_uint32(tx["lock_time"]) +
            serialize_uint32(sighash_type)
        )


