#!/usr/bin/env python3

import sys
sys.path.append("..")

from litcoin.binhex import b, x
from litcoin.address import make_p2sh_address
from litcoin.outpoint import make_outpoint
from litcoin.txid import make_txid
from examples.utils import input_ans, input_network_name
from blockchain import blockexplorer
from blockchain.exceptions import APIException
from examples.utils import input_private_key

def rev_txid_str(txid_str):
    """
    Because blockexplorer returns the txid backwards (thanks)
    """
    rev = ''
    i = len(txid_str) - 2
    while i >= 0:
        rev += txid_str[i : i + 2]
        i -= 2
    return rev


def get_utxos(address):
    """
    Get all the UTXOs for an address. 
    TODO: Remove dependency on blockexplorer and use litcoin instead
    """
    utxos = []
    for out in blockexplorer.get_unspent_outputs(address):
        utxos.append({
            "outpoint": make_outpoint(make_txid(rev_txid_str(out.tx_hash)), out.tx_output_n),
            "value": out.value
        })
    return utxos


def get_total_value(utxos):
    total_value = 0
    for utxo in utxos:
        total_value += utxo["value"]
    return total_value


def main():
    network_name = input_network_name()
    redeem_script = b(input("Redeem script ?"))
    p2sh_address = make_p2sh_address(redeem_script, network_name)

    print("Searching for UTXOs for address {0}...".format(p2sh_address)),
    utxos = get_utxos(p2sh_address)
    total_value = get_total_value(utxos)

    print("Found {0}s in {1} UTXOs:".format(total_value, len(utxos)))
    for utxo in utxos:
        print("    {0}s stored in {1}:{2}".format(
            utxo["value"],
            x(utxo["outpoint"]["txid"]),
            utxo["outpoint"]["output_index"]
        ))

    if total_value == 0:
        print("Exiting")
        sys.exit(0)

    privkey = input_private_key(network_name)
    deposit_address = input("Deposit address ?")
    

if __name__ == "__main__":
    main()
