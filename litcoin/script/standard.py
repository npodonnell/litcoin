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

from litcoin.address import address_decode
from litcoin.script.compiler import compile_script
from litcoin.script.operations import OP_DUP, OP_HASH160, OP_EQUALVERIFY, OP_EQUAL, OP_CHECKSIG
from litcoin.symbols import ADDRESS_TYPE_P2PKH, ADDRESS_TYPE_P2SH
from litcoin.hashing import validate_hash160
from litcoin.binhex import b


def make_p2pkh_locking_script(pubkey_hash):
    """
    Makes a P2PKH (Pay-to-public-key-hash) script which pays to pubkey_hash.
    """
    validate_hash160(pubkey_hash)
    return [OP_DUP, OP_HASH160, pubkey_hash, OP_EQUALVERIFY, OP_CHECKSIG]


def make_p2sh_locking_script(script_hash):
    """
    Makes a P2SH (Pay-to-script-hash) script which pays to script_hash.
    """
    validate_hash160(script_hash)
    return [OP_HASH160, script_hash, OP_EQUAL]


def make_std_locking_script(address):
    """
    Makes either a P2PKH (Pay-to-public-key-hash) or P2SK (Pay-to-script-hash)
    script depending on the address type.
    """
    _, address_type, address_hash = address_decode(address)

    if address_type == ADDRESS_TYPE_P2PKH:
        return make_p2pkh_locking_script(address_hash)
    elif address_type == ADDRESS_TYPE_P2SH:
        return make_p2sh_locking_script(address_hash)


def make_p2sh_unlocking_script(redeem_script, scriptsig_script=[]):
    """
    Makes a P2SH (Pay-to-script-hash) unlocking script.
    """
    assert type(redeem_script) in (list, str, bytes)
    assert type(scriptsig_script) is list

    if type(redeem_script) is list:
        redeem_script = compile_script(redeem_script)
    elif type(redeem_script) is str:
        redeem_script = b(redeem_script)

    return scriptsig_script + [redeem_script]
