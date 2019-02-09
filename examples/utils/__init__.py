#!/usr/bin/env python3

import sys
sys.path.append('../..')


from litcoin.networks import NETWORK_NAMES


def get_ans(question):
    """
    Prompt user to answer Y/N question from console
    """
    while True:
        ans = input(question + '(y/n)? ')
        letter = ans.lower()[0]

        if letter == 'n':
            return False
        if letter == 'y':
            return True


def get_network_name():
    """
    Prompt user to choose a network
    """
    while True:
        network_name = input('network ({0}) ? '.format(','.join(NETWORK_NAMES)))
        if network_name in NETWORK_NAMES:
            return network_name
