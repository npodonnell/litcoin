#!/usr/bin/env python3

NETWORKS = {
    'bitcoin': {
        'name': 'Bitcoin',
        'inventor': 'Satoshi Nakamoto',
        'p2pkh_prefix': b'\x00'
    },
    'litecoin': {
        'name': 'Litecoin',
        'inventor': 'Charles Lee',
        'p2pkh_prefix': b'\x30'
    }
}

def get_p2pkh_prefix(network_name):
    return NETWORKS[network_name]['p2pkh_prefix']
