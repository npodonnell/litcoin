#!/usr/bin/env python3

from litcoin.networks import NETWORKS, NETWORK_NAMES, network_inventor, \
	network_p2pkh_prefix, network_p2sh_prefix, network_wif_prefix
import unittest


class TestBinHex(unittest.TestCase):
	def test_NETWORK_KEYS(self):
		assert(set(NETWORK_NAMES) == set(NETWORKS.keys()))
	

	def test_network_inventor(self):
	    for key in NETWORK_NAMES:
	        assert network_inventor(key) == NETWORKS[key]['inventor']


	def test_network_p2pkh_prefix(self):
	    for key in NETWORK_NAMES:
	        assert network_p2pkh_prefix(key) == NETWORKS[key]['p2pkh_prefix']


	def test_network_p2sh_prefix(self):
	    for key in NETWORK_NAMES:
	        assert network_p2sh_prefix(key) == NETWORKS[key]['p2sh_prefix']


	def test_network_wif_prefix(self):
	    for key in NETWORK_NAMES:
	        assert network_wif_prefix(key) == NETWORKS[key]['wif_prefix']
