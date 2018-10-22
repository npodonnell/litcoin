#!/usr/bin/env python3

from litcoin.networks import NETWORKS, network_name, network_inventor, network_p2pkh_prefix, network_p2sh_prefix
import unittest


NETWORK_KEYS = list(NETWORKS.keys())


class TestBinHex(unittest.TestCase):
	def test_network_name(self):
	    for key in NETWORK_KEYS:
	        assert network_name(key) == NETWORKS[key]['name']


	def test_network_inventor(self):
	    for key in NETWORK_KEYS:
	        assert network_inventor(key) == NETWORKS[key]['inventor']


	def test_network_p2pkh_prefix(self):
	    for key in NETWORK_KEYS:
	        assert network_p2pkh_prefix(key) == NETWORKS[key]['p2pkh_prefix']


	def test_network_p2sh_prefix(self):
	    for key in NETWORK_KEYS:
	        assert network_p2sh_prefix(key) == NETWORKS[key]['p2sh_prefix']
