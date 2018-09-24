#!/usr/bin/env python3

from litcoin.keys import make_keypair
from litcoin.address import make_address

def make_wallet(**kwargs):
    """
    Make a wallet

    kwargs:
    network (string, required) - name of the network for which to create the wallet (eg. BITCOIN, LITECOIN)
    passphrase (string, optional) - brainwallet passphrase for generating private key
    """

    keypair = make_keypair()

    return {
        'pubkey': keypair['pubkey'],
        'privkey': keypair['privkey'],
        'address': make_address(keypair['pubkey'])
    }