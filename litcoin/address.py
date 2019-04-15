#!/usr/bin/env python3

from .hashing import hash160, double_sha
from .base58check import base58check_encode, base58check_decode
from .networks import NETWORKS
from .symbols import ADDRESS_TYPE_P2PKH, ADDRESS_TYPE_P2SH

ADDRESS_DECODED_EXPECTED_LENGTH_IN_BYTES = 21



def make_p2pkh_address(pubkey, network_name):
    pubkey_hash = hash160(pubkey)
    prefixed_pubkey_hash = NETWORKS[network_name]['p2pkh_prefix'] + pubkey_hash
    addr = base58check_encode(prefixed_pubkey_hash)
    return addr


def make_p2sh_address(script, network_name):
    script_hash = hash160(script)
    prefixed_script_hash = NETWORKS[network_name]['p2sh_prefix'] + script_hash
    address = base58check_encode(prefixed_script_hash)
    return address


def address_decode(address):
    """
    Decode an address, extract the prefix and return a tuple of the
    network name, address type, and the hash
    """
    decoded = base58check_decode(address)
    assert len(decoded) == ADDRESS_DECODED_EXPECTED_LENGTH_IN_BYTES, \
        "Decoded address should be of length {0}".format(ADDRESS_DECODED_EXPECTED_LENGTH_IN_BYTES)
    
    address_prefix = int.from_bytes(decoded[:1], byteorder='big', signed=False)
    address_hash = decoded[1:]
    decoded = False

    for network_name in NETWORKS:
        network = NETWORKS[network_name]
        if address_prefix in network["address_prefixes"]:
            address_network_name = network["name"]
            address_type = network["address_prefixes"][address_prefix]
            decoded = True
            break

    if not decoded:
        raise ValueError("Unable to decode address prefix {0} from address {1}".format(address_prefix, address))
    
    return (address_network_name, address_type, address_hash)
