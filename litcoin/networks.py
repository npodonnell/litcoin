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


def get_name(key):
    return NETWORKS[key]['name']


def get_inventor(key):
    return NETWORKS[key]['inventor']


def get_p2pkh_prefix(key):
    return NETWORKS[key]['p2pkh_prefix']


def get_p2sh_prefix(key):
    return NETWORKS[key]['p2sh_prefix']