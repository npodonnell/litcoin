#!/usr/bin/env python3

import sys
sys.path.append('../..')

from litcoin.networks import NETWORK_NAMES
from litcoin.ec import make_privkey, derive_pubkey
from litcoin.address import make_p2pkh_address
from litcoin.wif import privkey_to_wif
from litcoin.binhex import x

print('Available networks: {0}'.format(NETWORK_NAMES))

while True:
    network = input('network?')
    if network in NETWORK_NAMES:
        break

passphrase = input('Brainwallet passphrase?')


privkey = make_privkey(passphrase=passphrase)
pubkey = derive_pubkey(privkey)
address = make_p2pkh_address(pubkey, network=network)
wif_privkey = privkey_to_wif(privkey, False, network)


print('Private Key (WIF): {0}'.format(wif_privkey))
print('Public Key: {0}'.format(x(pubkey)))
print('Address: {0}'.format(address))
