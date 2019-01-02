#!/usr/bin/env python3

from litcoin.hashing import hash160, double_sha
from litcoin.base58check import base58check_encode, base58check_decode
from litcoin.networks import NETWORK_NAMES, NETWORK_BY_P2PKH_PREFIX, network_p2pkh_prefix


def make_p2pkh_address(pubkey, network=NETWORK_NAMES[0]):
    pubkey_hash = hash160(pubkey)
    prefixed_pubkey_hash = network_p2pkh_prefix(network) + pubkey_hash
    address = base58check_encode(prefixed_pubkey_hash)
    return address


def address_to_network(addr):
    decoded = base58check_decode(addr)
    prefix = decoded[0:1]
    return NETWORK_BY_P2PKH_PREFIX[prefix]


def make_p2sh_address(script, network=NETWORK_NAMES[0]):
    pass
