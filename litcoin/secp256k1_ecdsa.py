from hashlib import sha256
from .secp256k1 import SECP256K1_ORDER, SECP256K1_ORDER_HALVED, secp256k1_random_scalar, secp256k1_add, secp256k1_multiply, secp256k1_order_inverse
from .rfc6979 import generate_k
from .uint256 import uint256_from_bytes


def secp256k1_ecdsa_sign(privkey: int, msg_hash: bytes, counter: int = 0) -> tuple[int, int]:
    """Sign with deterministic generation of k."""
    if counter > 0:
        ee = counter.to_bytes(32, byteorder="little", signed=False)
    else:
        ee = b""
    k: int = generate_k(SECP256K1_ORDER, privkey, sha256, msg_hash, 0, ee)
    m: int = uint256_from_bytes(msg_hash)
    r: int = secp256k1_multiply(k)[0]
    s: int = (((m + (privkey * r)) % SECP256K1_ORDER) * secp256k1_order_inverse(k)) % SECP256K1_ORDER
    if SECP256K1_ORDER_HALVED < s:
        return r, SECP256K1_ORDER - s
    return r, s


def secp256k1_ecdsa_verify(sig: tuple[int, int], pubkey: tuple[int, int], msg_hash: bytes) -> bool:
    """Verify signature."""
    m: int = uint256_from_bytes(msg_hash)
    r, s = sig
    s_inv: int = secp256k1_order_inverse(s)
    u_1: int = (s_inv * m) % SECP256K1_ORDER
    u_2: int = (s_inv * r) % SECP256K1_ORDER
    point_p: tuple[int, int] = secp256k1_add(secp256k1_multiply(u_1), secp256k1_multiply(u_2, pubkey))
    return point_p[0] == r
