#!/usr/bin/env python3

import ctypes
import ctypes.util

_ssl = ctypes.cdll.LoadLibrary(ctypes.util.find_library('ssl') or 'libeay32')

POINT_CONVERSION_COMPRESSED = 2
POINT_CONVERSION_UNCOMPRESSED = 4
NID_secp256k1 = 714

class OpenSSLException(EnvironmentError):
    pass

# Thx to Sam Devlin for the ctypes magic 64-bit fix.
def _check_result (val, func, args):
    if val == 0:
        raise ValueError
    else:
        return ctypes.c_void_p (val)

_ssl.EC_KEY_new_by_curve_name.restype = ctypes.c_void_p
_ssl.EC_KEY_new_by_curve_name.errcheck = _check_result

def make_keypair(**kwargs):
    # TODO: consider passphrase
    def get_privkey(k):
        # TODO: write custom code to generate random numbers - don't rely on OpenSSL to
        # generate random numbers
        size = _ssl.i2d_ECPrivateKey(k, 0)
        buf = ctypes.create_string_buffer(size)
        _ssl.i2d_ECPrivateKey(k, ctypes.byref(ctypes.pointer(buf)))
        return buf.raw
    
    def get_pubkey(k):
        size = _ssl.i2o_ECPublicKey(k, 0)
        buf = ctypes.create_string_buffer(size)
        _ssl.i2o_ECPublicKey(k, ctypes.byref(ctypes.pointer(buf)))
        return buf.raw

    k = _ssl.EC_KEY_new_by_curve_name(NID_secp256k1)
    if _ssl.EC_KEY_generate_key(k) != 1:
        raise OpenSSLException('Error generating keypair')

    privkey = get_privkey(k)
    pubkey = get_pubkey(k)

    _ssl.EC_KEY_free(k)

    return {
        'privkey': privkey,
        'pubkey': pubkey
    }