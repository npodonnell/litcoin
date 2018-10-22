#!/usr/bin/env python3

from litcoin.networks import NETWORKS, network_name, network_inventor, network_p2pkh_prefix, network_p2sh_prefix

NETWORK_KEYS = list(NETWORKS.keys())


def test_network_name():
    for key in NETWORK_KEYS:
        assert network_name(key) == NETWORKS[key]['name']


def test_network_inventor():
    for key in NETWORK_KEYS:
        assert network_inventor(key) == NETWORKS[key]['inventor']


def test_network_p2pkh_prefix():
    for key in NETWORK_KEYS:
        assert network_p2pkh_prefix(key) == NETWORKS[key]['p2pkh_prefix']


def test_network_p2sh_prefix():
    for key in NETWORK_KEYS:
        assert network_p2sh_prefix(key) == NETWORKS[key]['p2sh_prefix']
