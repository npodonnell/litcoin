
# 🔥**Lit**coin
A library for interacting with Bitcoin and Litecoin (and possibly more similar cryptocurrencies in the future)


## Tenets

* Abstract all the commonalities of these cryptocurrencies and parameterize functions with the name of the network in question.
* Use simple data structures such as `bytes`, `str`, `list` and `dict` instead of `class`.
* Be easy to translate into other languages.
* Have as few dependencies as possible.
* **Be a central point of failure, but don't fail**.
* Be functional.
* Abstract all 3rd party code
* Test everything.

## License
MIT

## Build / Install

To develop or experiment with litcoin, we recommend using virtual environments. 

Create and initalize a virtual environment:
```
virtualenv -p python3 venv
. venv/bin/activate
```

Install pytest:
```
pip3 install pytest
```

Build:
```
./setup.py build
```

Run Tests:
```
pytest
```

Install:
```
pip install .
```

## Usage

Creating keys and addresses
```
>>> from litcoin.address import make_p2pkh_address
>>> from litcoin.ec import make_privkey, derive_pubkey
>>> privkey = make_privkey()
>>> privkey
b'\xc5\xaeYw\xf5\x9e\xa9-\x9a\x11\x88Vd5\xccg/<\xae\xa6e\xbf\x85\xa2\xfb\x92=\xe8:\xe0$\x0e'
>>> pubkey = derive_pubkey(privkey)
>>> laddr = make_p2pkh_address(pubkey, network='litecoin')
>>> baddr = make_p2pkh_address(pubkey, network='bitcoin')
>>> laddr
'LL8SyH86F6SeKZPDBWDYpFcQg4v775yG9v'
>>> baddr
'1uVi4pGASCb4kh41NEFYEYeTrYpyhfULL'
```
