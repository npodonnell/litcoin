#!/usr/bin/env python3

import sys
sys.path.append('..')

from litcoin.ec import make_privkey, derive_pubkey
from litcoin.address import make_p2pkh_address
from litcoin.wif import privkey_to_wif
from litcoin.binhex import x
from examples.utils import get_ans, get_network_name


def main():
    network_name = get_network_name()
    passphrase = input('Brainwallet passphrase? ')
    compress = get_ans('Compress pubkey')

    privkey = make_privkey(passphrase=passphrase)
    pubkey = derive_pubkey(privkey, compress)
    address = make_p2pkh_address(pubkey, network_name)
    wif_privkey = privkey_to_wif(privkey, compress, network_name)

    print('Private Key (WIF): {0}'.format(wif_privkey))
    print('Public Key: {0}'.format(x(pubkey)))
    print('Address: {0}'.format(address))

if __name__ == '__main__':
    main()
