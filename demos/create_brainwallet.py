#!/usr/bin/env python3

import sys
sys.path.append('..')

from litcoin.networks import NETWORK_NAMES
from litcoin.ec import make_privkey, derive_pubkey
from litcoin.address import make_p2pkh_address
from litcoin.wif import privkey_to_wif
from litcoin.binhex import x


def get_ans(question):
    """
    Gets the answer to a Y/N question
    """
    while True:
        ans = input(question + '(y/n)? ')
        letter = ans.lower()[0]

        if letter == 'n':
            return False
        if letter == 'y':
            return True


def main():
    print('Available networks: {0}'.format(NETWORK_NAMES))

    while True:
        network = input('network? ')
        if network in NETWORK_NAMES:
            break

    passphrase = input('Brainwallet passphrase? ')
    compress = get_ans('Compress pubkey')

    privkey = make_privkey(passphrase=passphrase)
    pubkey = derive_pubkey(privkey, compress)
    address = make_p2pkh_address(pubkey, network=network)
    wif_privkey = privkey_to_wif(privkey, compress, network)

    print('Private Key (WIF): {0}'.format(wif_privkey))
    print('Public Key: {0}'.format(x(pubkey)))
    print('Address: {0}'.format(address))

if __name__ == '__main__':
    main()