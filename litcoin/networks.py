#!/usr/bin/env python3

from .binhex import b

NETWORKS = {
    'bitcoin': {
        'inventor': 'Satoshi Nakamoto',
        'p2pkh_prefix': b'\x00',
        'p2sh_prefix': b'\x05',
        'wif_prefix': b'\x80'
    },
    'litecoin': {
        'inventor': 'Charles Lee',
        'p2pkh_prefix': b'\x30',
        'p2sh_prefix': b'\x05',
        'wif_prefix': b'\xb0'
    }
}


NETWORK_NAMES = list(NETWORKS.keys())


NETWORK_BY_P2PKH_PREFIX = {
    b('00'): 'bitcoin',
    b('30'): 'litecoin'
}


def get_network(network_name):
    try:
        return NETWORKS[network_name]
    except:
        raise ValueError('Unknown network: {0}'.format(network_name))


def network_inventor(key):
    return NETWORKS[key]['inventor']


def network_p2pkh_prefix(key):
    return NETWORKS[key]['p2pkh_prefix']


def network_p2sh_prefix(key):
    return NETWORKS[key]['p2sh_prefix']


def network_wif_prefix(key):
    return NETWORKS[key]['wif_prefix']
