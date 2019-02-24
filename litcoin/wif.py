#!/usr/bin/env python3

from litcoin.networks import NETWORKS
from litcoin.base58check import base58check_encode, base58check_decode


def privkey_to_wif(privkey, is_compressed_pubkey, network_name):
    wif_data = NETWORKS[network_name]['wif_prefix'] + \
        privkey + (b'\x01' if is_compressed_pubkey else b'')
    return base58check_encode(wif_data)


def wif_to_privkey(wif, network_name):
    decoded = base58check_decode(wif)
    decoded_len = len(decoded)

    assert decoded_len == 33 or decoded_len == 34, \
        'decoded WIF should be 33 or 34 bytes but was {0} bytes'.format(decoded_len)

    wif_prefix = decoded[0:1]

    if network_name != None:
        assert wif_prefix == NETWORKS[network_name]['wif_prefix'], \
            'unknown WIF prefix for network {0}: {1}'.format(network_name, wif_prefix)
        
    if decoded_len == 34:
        assert decoded[-1:] == b'\x01', 'last byte in decoded 34-byte WIF should be 0x01'
        return decoded[1:-1]
    else:
        return decoded[1:]
