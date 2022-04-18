from hashlib import sha256
from .secp256k1 import SECP256K1_ORDER, secp256k1_random_scalar, secp256k1_multiply, secp256k1_order_inverse
from .rfc6979 import generate_k
from .uint256 import uint256_from_bytes


def secp256k1_ecdsa_sign(privkey: int, msg_hash: bytes) -> tuple[int, int]:
    """Sign with deterministic generation of k."""
    k: int = generate_k(SECP256K1_ORDER, privkey, sha256, msg_hash)
    r: int = secp256k1_multiply(k)[0]
    s: int = (((uint256_from_bytes(msg_hash) + ((privkey * r) % SECP256K1_ORDER)) % SECP256K1_ORDER) * secp256k1_order_inverse(k)) % SECP256K1_ORDER
    return r, s
