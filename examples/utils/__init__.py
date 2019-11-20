#!/usr/bin/env python3

import sys
from getpass import getpass
sys.path.append('../..')

from litcoin.networks import NETWORK_NAMES
from litcoin.wif import wif_to_privkey
from litcoin.ec import validate_pubkey
from litcoin.binhex import b


def input_ans(question):
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


def input_passphrase():
    """
    Prompt user for passphrase
    """
    passphrase = input('Passphrase (leave blank for none) ?')
    if len(passphrase) == 0:
        return None
    else:
        return passphrase


def input_network_name():
    """
    Prompt user to choose a network
    """
    while True:
        network_name = input('network ({0})?'.format(','.join(NETWORK_NAMES)))
        if network_name in NETWORK_NAMES:
            return network_name


def input_public_key():
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


def input_private_key(network_name):
    """
    Prompt user to input a private key
    """
    try:
        data = getpass("Private key?")
        return wif_to_privkey(data, network_name)
    except:
        raise ValueError("Invalid WIF key for the {0} network".format(network_name))
