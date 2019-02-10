#!/usr/bin/env python3

import sys
sys.path.append('..')

import time
from datetime import datetime
from blockchain import blockexplorer
from litcoin.script.constants import LOCKTIME_THRESHOLD
from litcoin.networks import NETWORKS
from examples.utils import get_ans, get_network_name, get_public_key


def get_date_or_block_height(seconds_per_block):
    print('How do you wish to specify the lock time ?')
    print('1. Timestamp')
    print('2. Chain Height')

    while True:
        choice = input('Choice ?')
        if choice == '1':
            while True:
                datetime_str = input('UTC Date and Time (YYYY/MM/DD HH:MM:SS) ?')
                unix_ts = int(time.mktime(datetime.strptime(datetime_str, '%Y/%m/%d %H:%M:%S').utctimetuple()))
                if unix_ts <= LOCKTIME_THRESHOLD:
                    print('Datetime is too early and would be interpreted as a block height')
                    continue
                return unix_ts
        elif choice == '2':
            while True:
                block_height = int(input('Block Height(0..{0}) ?'.format(LOCKTIME_THRESHOLD)))
                if block_height < 0 or LOCKTIME_THRESHOLD < block_height:
                    print('Block height should be in the range 0..{0}'.format(LOCKTIME_THRESHOLD))
                    continue
                return block_height
        else:
            print('Invalid choice')
            continue


def main():
    network_name = get_network_name()
    network = NETWORKS[network_name]
    pubkey = get_public_key()
    date_or_block_height = get_date_or_block_height(network['seconds_per_block'])


if __name__ == '__main__':
    main()
