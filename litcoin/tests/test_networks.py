#!/usr/bin/env python3

from litcoin.networks import NETWORKS
import unittest


class TestNetworks(unittest.TestCase):
    def test_NETWORKS(self):
        assert(set(NETWORKS.keys()) == set(['bitcoin', 'litecoin']))

        for network_name in NETWORKS:
            network = NETWORKS[network_name]
            assert(set(network.keys()) == set(['name', 'inventor', 'address_prefixes', 'p2pkh_prefix', 'p2sh_prefix', 'wif_prefix', \
                'seconds_per_block', 'seconds_between_retargets', 'blocks_between_halving', 'genesis_block'])), \
                '`network.keys()` should contain correct properties for network {0}'.format(network_name)
            assert type(network_name) is str, '`network_name` should be of type str for network {0}'.format(network_name)
            assert type(network) is dict, '`network` should be of type dict for network {0}'.format(network_name)
            assert type(network['name']) is str, '`network[\'name\']` should be of type str for network {0}'.format(network_name)
            assert network_name == network['name'], 'network_name should be equal to network[\'name\'] for network {0}'.format(network_name)
            assert type(network['seconds_per_block']) is int, '`network[\'seconds_per_block\']` should be of type int for network {0}'.format(network_name)
            assert 0 < network['seconds_per_block'], '`network[\'seconds_per_block\']` should be greater than zero for network {0}'.format(network_name)
            assert 0 < network['seconds_between_retargets'], '`network[\'seconds_between_retargets\']` should be greater than zero for network {0}'.format(network_name)
            assert 0 < network['blocks_between_halving'], '`network[\'blocks_between_halving\']` should be greater than zero for network {0}'.format(network_name)
            
            genesis_block = network['genesis_block']
            assert set(genesis_block.keys()) == set(['time', 'nonce']), '`network[\'genesis_block\'].keys()` should contain correct properties for network {0}'.format(network_name)
            assert 0 < genesis_block['time'], '`genesis_block[\'time\']` should be greater than zero for network {0}'.format(network_name)
            assert 0 < genesis_block['nonce'], '`genesis_block[\'nonce\']` should be greater than zero for network {0}'.format(network_name)
