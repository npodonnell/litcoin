#!/usr/bin/env python3

from litcoin.binhex import b

NETWORKS = {
    'bitcoin': {
        'name': 'bitcoin',
        'inventor': 'Satoshi Nakamoto',
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
        'p2pkh_prefix': b('30'),
        'p2sh_prefix': b('05'),
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

# reverse lookups

NETWORK_BY_P2PKH_PREFIX = {
    NETWORKS[k]['p2pkh_prefix']: NETWORKS[k] for k in NETWORKS
}

"""
Note that there should be **no** NETWORK_BY_P2SH_PREFIX since
bitcoin and litecoin have the same prefix (0x05)
"""
