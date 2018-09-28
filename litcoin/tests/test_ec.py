#!/usr/bin/env python3

from litcoin.ec import compress_ec_point, make_privkey, derive_pubkey, sign_message, verify_signature


def test_compress_ec_point():
    actual = compress_ec_point(0, 0)
    expected = bytes.fromhex('020000000000000000000000000000000000000000000000000000000000000000')
    assert actual == expected

    actual = compress_ec_point(0, 1)
    expected = bytes.fromhex('030000000000000000000000000000000000000000000000000000000000000000')
    assert actual == expected

    actual = compress_ec_point(1, 0)
    expected = bytes.fromhex('020000000000000000000000000000000000000000000000000000000000000001')
    assert actual == expected

    actual = compress_ec_point(1, 1)
    expected = bytes.fromhex('030000000000000000000000000000000000000000000000000000000000000001')
    assert actual == expected

    actual = compress_ec_point(1, 1)
    expected = bytes.fromhex('030000000000000000000000000000000000000000000000000000000000000001')
    assert actual == expected


def test_make_privkey():
    for _ in range(0, 1000):
        privkey1 = make_privkey()
        privkey2 = make_privkey()
        assert type(privkey1) == bytes
        assert type(privkey2) == bytes
        assert len(privkey1) == 32
        assert len(privkey2) == 32
        assert privkey1 != privkey2

    actual = make_privkey(passphrase='')
    expected = bytes.fromhex('e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855')
    assert actual == expected

    actual = make_privkey(passphrase='bitcoin')
    expected = bytes.fromhex('6b88c087247aa2f07ee1c5956b8e1a9f4c7f892a70e324f1bb3d161e05ca107b')
    assert actual == expected

    actual = make_privkey(passphrase='litecoin')
    expected = bytes.fromhex('6ce9fe4549f0f60d6fcc7697681ec2e6ed2eade066c3f6829628a59ce5cfc64b')
    assert actual == expected

    actual = make_privkey(passphrase='litcoin')
    expected = bytes.fromhex('83154786b09476e9221d30bb1f98cb678c02bc8ddc97deeb654f6dcd93f95474')
    assert actual == expected


def test_derive_pubkey():
    actual = derive_pubkey(bytes.fromhex('7cf3547ccfbf3b17d3eae42256396c0544714b0df4f8c8c4268a3e2d705eaf73'))
    expected = bytes.fromhex('02172204d37ae71933f2595bc74eb90e984254759c560245d8bf523e0d60c1477b')
    assert actual == expected

    actual = derive_pubkey(bytes.fromhex('0ec786c41a15ced8b1d018539cdcbdc50c40e733a9ba6775ce5733d75bb78a42'))
    expected = bytes.fromhex('032be7848317b80628112869f4da0edfbc1f4ca9539a8c94355bad5961a36d33d6')
    assert actual == expected


def test_sign_message():
    pass


def test_verify_message():
    pass
