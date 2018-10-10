
# **Lit**coin

A library for interacting with Bitcoin and Litecoin (and possibly more similar cryptocurrencies in the future)


<span style="color:red">
<h2>
<b>
<center>
WARNING: THIS LIBRARY IS UNDER CONSTRUCTION. DO NOT USE IT FOR COMMERCIAL PURPOSES. YOU MAY LOSE MONEY
</center>
</b>
</h2>
</span>


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

## Installation

Install these first:
```
sudo pip3 install setuptools
sudo pip3 install pytest
sudo pip3 install pytest-runner
sudo pip3 install cryptography
```

Build:
```
./setup.py build
```

Run Tests:
```
./setup.py test
```

Install:
```
sudo ./setup.py install
```

## Usage

Creating keys and addresses
```
Python 3.6.5 (default, Apr  4 2018, 15:09:05) 
[GCC 7.3.1 20180130 (Red Hat 7.3.1-2)] on linux
Type "help", "copyright", "credits" or "license" for more information.
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
