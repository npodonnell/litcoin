#!/usr/bin/env python3

NETWORKS = {
    'bitcoin': {
        'name': 'Bitcoin',
        'inventor': 'Satoshi Nakamoto',
        'p2pkh_prefix': b'\x00',
        'p2sh_prefix': b'\x05'
    },
    'litecoin': {
        'name': 'Litecoin',
        'inventor': 'Charles Lee',
        'p2pkh_prefix': b'\x30',
        'p2sh_prefix': b'\x05'
    }
}

NETWORK_KEYS = list(NETWORKS.keys())


def network_name(key):
    return NETWORKS[key]['name']


def network_inventor(key):
    return NETWORKS[key]['inventor']


def network_p2pkh_prefix(key):
    return NETWORKS[key]['p2pkh_prefix']


def network_p2sh_prefix(key):
    return NETWORKS[key]['p2sh_prefix']
