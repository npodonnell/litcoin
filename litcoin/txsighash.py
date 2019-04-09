#!/usr/bin/env python3

from .tx import tx_copy
from .script.compiler import compile_script
from .script.operations import OP_CODESEPARATOR
from .binhex import b, x
from .hashing import double_sha
from .outpoint import serialize_outpoint
from .txoutput import serialize_txoutput, make_txoutput
from .script.serialization import serialize_script
from .uint32 import serialize_uint32
from .int64 import serialize_int64
from .varint import serialize_varint

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

# Pre-compute serializations which are used often
EMPTY_SCRIPT = compile_script([])
SERIALIZED_EMPTY_SCRIPT = serialize_script(EMPTY_SCRIPT)
SERIALIZED_NULL_TXOUTPUT = serialize_txoutput(make_txoutput(-1, EMPTY_SCRIPT))


def sigversion_base_serialize(tx, script, input_index, sighash_type, anyone_can_pay, 
    hash_single, hash_none):
    """
    Base tx serializer
    See CTransactionSignatureSerializer::Serialize in src/script/interpreter.cpp
    """
    sig = serialize_uint32(tx["version"])
    n_inputs = 1 if anyone_can_pay else len(tx["inputs"])
    sig += serialize_varint(n_inputs)

    for n_input in range(n_inputs):
        # See CTransactionSignatureSerializer::SerializeInput
        if anyone_can_pay:
            n_input = input_index
        sig += serialize_outpoint(tx["inputs"][n_input]["outpoint"])

        if n_input != input_index:
            sig += SERIALIZED_EMPTY_SCRIPT
        else:
            sig += serialize_script(script)

        if n_input != input_index and (hash_single or hash_none):
            sig += serialize_uint32(0)
        else:
            sig += serialize_uint32(tx["inputs"][n_input]["sequence_no"])
    
    n_outputs = 0 if hash_none else input_index + 1 if hash_single else len(tx["outputs"])
    sig += serialize_varint(n_outputs)

    for n_output in range(n_outputs):
        # See CTransactionSignatureSerializer::SerializeOutput
        if hash_single and n_output != input_index:
            sig += SERIALIZED_NULL_TXOUTPUT
        else:
            sig += serialize_txoutput(tx["outputs"][n_output])
    
    sig += serialize_uint32(tx["lock_time"])
    return sig


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
    assert sigversion == SIGVERSION_BASE or sigversion == SIGVERSION_WITNESS_V0, \
        "`sigversion` should be either `SIGVERSION_BASE` or `SIGVERSION_WITNESS_V0`"

    anyone_can_pay = sighash_type & SIGHASH_ANYONECANPAY
    hash_single = sighash_type & 0x1f == SIGHASH_SINGLE
    hash_none = sighash_type & 0x1f == SIGHASH_NONE

    if sigversion == SIGVERSION_WITNESS_V0:
        hash_prevouts = b('0000000000000000000000000000000000000000000000000000000000000000')
        hash_sequence = b('0000000000000000000000000000000000000000000000000000000000000000')
        hash_outputs = b('0000000000000000000000000000000000000000000000000000000000000000')

        if not anyone_can_pay:
            hash_prevouts = get_prevout_hash(tx)
            if not hash_single and not hash_none:
                hash_sequence = get_sequence_hash(tx)
        if not hash_single and not hash_none:
            hash_outputs = get_outputs_hash(tx)
        elif hash_single and input_index < len(tx["outputs"]):
            hash_outputs = double_sha(serialize_txoutput(tx["outputs"][input_index]))
        
        return double_sha(
            serialize_uint32(tx["version"]) +
            hash_prevouts +
            hash_sequence +
            serialize_outpoint(tx["inputs"][input_index]["outpoint"]) +
            serialize_script(script) +
            serialize_int64(amount) +
            serialize_uint32(tx["inputs"][input_index]["sequence_no"]) +
            hash_outputs +
            serialize_uint32(tx["lock_time"]) +
            serialize_uint32(sighash_type)
        )
    
    if hash_single:
        if len(tx["inputs"]) <= input_index:
            return HASH_ONE

    return double_sha(
        sigversion_base_serialize(tx, script, input_index, sighash_type, anyone_can_pay, hash_single, hash_none) +
        serialize_uint32(sighash_type)
    )
