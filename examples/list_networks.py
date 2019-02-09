#!/usr/bin/env python3

import sys
sys.path.append('..')

from litcoin.networks import NETWORKS


def main():
    print('Available networks are:')
    for network_name in NETWORKS:
        inventor = NETWORKS[network_name]['inventor']
        print('{0} (invented by {1})'.format(network_name, inventor))

    
if __name__ == '__main__':
    main()
