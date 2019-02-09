#!/usr/bin/env python3

from litcoin.binhex import b

NETWORKS = {
    'bitcoin': {
        'inventor': 'Satoshi Nakamoto',
        'p2pkh_prefix': b('00'),
        'p2sh_prefix': b('05'),
        'wif_prefix': b('80')
    },
    'litecoin': {
        'inventor': 'Charles Lee',
        'p2pkh_prefix': b('30'),
        'p2sh_prefix': b('05'),
        'wif_prefix': b('b0')
    }
}


NETWORK_NAMES = set(NETWORKS.keys())


NETWORK_BY_P2PKH_PREFIX = {
    b('00'): NETWORKS['bitcoin'],
    b('30'): NETWORKS['litecoin']
}
