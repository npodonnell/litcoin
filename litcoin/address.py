#!/usr/bin/env python3

from litcoin.hashing import hash160, double_sha
from litcoin.base58check import base58check_encode
from litcoin.networks import get_p2pkh_prefix


def make_p2pkh_address(pubkey, **kwargs):
    pubkey_hash = hash160(pubkey)
    prefixed_pubkey_hash = get_p2pkh_prefix(kwargs['network']) + pubkey_hash
    address = base58check_encode(prefixed_pubkey_hash)
    return address


def make_p2sh_address(script, **kwargs):
    pass