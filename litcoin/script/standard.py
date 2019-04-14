#!/usr/bin/env python3

"""
Functions for creating "standard" locking scripts for transaction outputs

Currently these are:
TX_PUBKEY: Pay to a public key (rarely used but needed for legacy compatibility)
TX_PUBKEYHASH: Pay to hash of a public key. Most common type of locking script.
TX_SCRIPTHASH: Pay to hash of a script (P2SH). The unlocking script will include a redeem script
               which acts as a drop-in replacement for the locking script and is executed at spend time.
TX_MULTISIG: Pay to M-of-N multiple signatures
TX_NULL_DATA: Unspendable OP_RETURN script that carries data.
TX_WITNESS_V0_SCRIPTHASH:
TX_WITNESS_V0_KEYHASH:
TX_WITNESS_UNKNOWN:
TX_NONSTANDARD
"""

from .operations import OP_DUP, OP_HASH160, OP_EQUALVERIFY, OP_EQUAL, OP_CHECKSIG
from ..hashing import validate_hash160


def make_p2pkh_locking_script(pubkey_hash):
    """
    Makes a P2PKH (Pay-to-public-key-hash) script which pays `amount` satoshis 
    to the public key which hashes to `pubkey_hash`
    """
    validate_hash160(pubkey_hash)
    return [OP_DUP, OP_HASH160, pubkey_hash, OP_EQUALVERIFY, OP_CHECKSIG]


def make_p2sh_locking_script(script_hash):
    """
    Makes a P2SH (Pay-to-script-hash) script which pays `amount` satoshis 
    to the redeem script which hashes to `script_hash`
    """
    validate_hash160(script_hash)
    return [OP_HASH160, script_hash, OP_EQUAL]
