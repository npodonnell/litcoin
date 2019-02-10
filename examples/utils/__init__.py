#!/usr/bin/env python3

import sys
sys.path.append('../..')

from litcoin.networks import NETWORK_NAMES
from litcoin.ec import validate_pubkey
from litcoin.binhex import b


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


def get_public_key():
    """
    Prompt user to input a public key
    """
    while True:
        try:
            pubkey = b(input('Public key?'))
            validate_pubkey(pubkey)
            return pubkey
        except AssertionError as ex:
            print(ex)
