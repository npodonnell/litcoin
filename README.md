# **Lit**coin

A library for interacting with Bitcoin and Litecoin (and possibly more similar cryptocurrencies in the future)

## Tenets

* Abstract all the commonalities of these cryptocurrencies and parameterize functions with the name of the network in question.
* Use simple data structures such as `bytes`, `str`, `list` and `dict` instead of `class`.
* Be easy to translate into other languages.
* Have as few dependencies as possible. In security-critical applications convenience is not a priority. The philosophy here is **Be a central point of failure, But don't fail**.
* Be functional.
* Test everything.

## License
MIT

## Prerequisites
* Python 3
* pip3

## Installation

Ensure you have setuptools installed:
```
sudo pip3 install setuptools
```

Build:
```
./setup.py build
```

Install:
```
sudo ./setup.py install
```

## Usage

Creating wallets
```
from litcoin.wallet import make_wallet

# Make a bitcoin wallet
bitcoin_wallet = make_wallet(network='bitcoin')

# Make a litecoin wallet
litecoin_wallet = make_wallet(network='litecoin')

# Make a bitcoin brainwallet
bitcoin_brainwallet = make_wallet(network='bitcoin', passphrase='abc123')

# Make a litecoin segwit wallet
litecoin_wallet = make_wallet(network='litecoin', segwit=True)
```

## Recipes
