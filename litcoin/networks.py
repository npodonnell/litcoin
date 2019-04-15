#!/usr/bin/env python3

from .binhex import b
from .symbols import ADDRESS_TYPE_P2PKH, ADDRESS_TYPE_P2SH

NETWORKS = {
    'bitcoin': {
        'name': 'bitcoin',
        'inventor': 'Satoshi Nakamoto',
        'address_prefixes': {
            0x00: ADDRESS_TYPE_P2PKH,
            0x05: ADDRESS_TYPE_P2SH
        },
        'p2pkh_prefix': b('00'),
        'p2sh_prefix': b('05'),
        'wif_prefix': b('80'),
        'seconds_per_block': int(10 * 60),
        'seconds_between_retargets': int(14 * 24 * 60 * 60),
        'blocks_between_halving': 210000,
        'genesis_block': {
            'time': 1231006505,
            'nonce': 2083236893
        }
    },
    'litecoin': {
        'name': 'litecoin',
        'inventor': 'Charles Lee',
        'address_prefixes': {
            0x30: ADDRESS_TYPE_P2PKH,
            0x32: ADDRESS_TYPE_P2SH
        },
        'p2pkh_prefix': b('30'),
        'p2sh_prefix': b('32'),
        'wif_prefix': b('b0'),
        'seconds_per_block': int(2.5 * 60),
        'seconds_between_retargets': int(3.5 * 24 * 60 * 60),
        'blocks_between_halving': 840000,
        'genesis_block': {
            'time': 1317972665,
            'nonce': 2084524493
        }
    }
}

NETWORK_NAMES = set(NETWORKS.keys())
