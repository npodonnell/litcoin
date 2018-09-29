#!/usr/bin/env python3

from litcoin.networks import NETWORKS, get_name, get_inventor, get_p2pkh_prefix, get_p2sh_prefix

NETWORK_KEYS = list(NETWORKS.keys())


def test_get_name():
    for key in NETWORK_KEYS:
        assert get_name(key) == NETWORKS[key]['name']


def test_get_inventor():
    for key in NETWORK_KEYS:
        assert get_inventor(key) == NETWORKS[key]['inventor']


def test_get_p2pkh_prefix():
    for key in NETWORK_KEYS:
        assert get_p2pkh_prefix(key) == NETWORKS[key]['p2pkh_prefix']


def test_get_p2sh_prefix():
    for key in NETWORK_KEYS:
        assert get_p2sh_prefix(key) == NETWORKS[key]['p2sh_prefix']
