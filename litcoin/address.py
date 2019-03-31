#!/usr/bin/env python3

from litcoin.hashing import hash160, double_sha
from litcoin.base58check import base58check_encode, base58check_decode
from litcoin.networks import NETWORKS, NETWORK_NAMES, NETWORK_BY_P2PKH_PREFIX

BASE58_DECODED_ADDRESS_EXPECTED_LENGTH = 21


def make_p2pkh_address(pubkey, network_name):
    pubkey_hash = hash160(pubkey)
    prefixed_pubkey_hash = NETWORKS[network_name]['p2pkh_prefix'] + pubkey_hash
    address = base58check_encode(prefixed_pubkey_hash)
    return address


def make_p2sh_address(script, network_name):
    script_hash = hash160(script)
    prefixed_script_hash = NETWORKS[network_name]['p2sh_prefix'] + script_hash
    address = base58check_encode(prefixed_script_hash)
    return address


def address_to_hash(addr):
    """
    Base58-decode an address, verify the length is 21 bytes (including prefix)
    then remove prefix and return 20-byte hash
    """
    decoded = base58check_decode(addr)
    assert len(decoded) == BASE58_DECODED_ADDRESS_EXPECTED_LENGTH, \
        "Length of decoded address should be of length {0}".format(BASE58_DECODED_ADDRESS_EXPECTED_LENGTH)
    return decoded[1:]


def address_to_network(addr):
    decoded = base58check_decode(addr)
    prefix = decoded[0:1]
    return NETWORK_BY_P2PKH_PREFIX[prefix]
