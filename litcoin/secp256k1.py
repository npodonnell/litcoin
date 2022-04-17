from .uint256 import uint256_random
from typing import Final
from math import inf


POINT_AT_INFINITY: Final[tuple[int, int]] = (inf, inf)

SECP256K1_P: Final[int] = 115792089237316195423570985008687907853269984665640564039457584007908834671663
SECP256K1_A: Final[int] = 0
SECP256K1_B: Final[int] = 7
SECP256K1_GENERATOR: Final[tuple[int, int]] = (
    55066263022277343669578718895168534326250603453777594175500187360389116729240,
    32670510020758816978083085130507043184471273380659243275938904335757337482424
)
SECP256K1_ORDER: Final[int] = 115792089237316195423570985008687907852837564279074904382605163141518161494337
SECP256K1_COFACTOR: Final[int] = 1


def _congruent(a: int, b: int, n: int) -> bool:
    """
    Returns true if a is congruent to b modulo n.
    """
    assert type(a) is int
    return (a % n) == (b % n)


def _egcd(a: int, b: int) -> tuple[int, int, int]:
    """
    Extended Euclidean Algorithm.
    """
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = _egcd(b % a, a)
        return g, x - (b // a) * y, y


def _mai(a: int, n: int) -> int:
    """
    Modular Additive Inverse (MAI) of a mod n.
    """
    return (n - a) % n


def _mmi(a: int, n: int) -> int:
    """
    Modular Mulplicative Inverse (MMI) of a mod n. 
    The MMI exists iff a and n are coprime.
    """
    assert(n >= 1)
    if a == 1 and n == 1:
        return 0
    else:
        g, x, _ = _egcd(a, n)
        if g == 1:
            return x % n
        elif g == -1:
            return _mai(x, n)
        else:
            raise ValueError(f"MMI does not exist for {a} modulo {n}")


def _mod_exp(a: int, x: int, n: int) -> int:
    """
    Fast modular exponentiation of a to the power x mod n.
    """
    if x == 0:
        return 1
    elif x == 1:
        return a % n
    elif x % 2 == 1:
        return (a * _mod_exp(a, x - 1, n)) % n
    else:
        return (_mod_exp(a, x >> 1, n) ** 2) % n


def _eulers_criterion(a: int, p: int) -> bool:
    """
    Euler's criterion says that an integer a is quadratic residue modulo an 
    odd prime p iff a^((p-1)/2) = 1 mod p. 
    Returns true if a satisfies Euler's criterion, i.e. if a is a quadratic 
    residue modulo n. 
    """
    assert type(a) is int
    return _mod_exp(a, (p - 1) >> 1, p) == 1


def _legendre_symbol(a: int, p: int) -> int:
    """
    Legendre symbol is a number which is 1 if a is a quadratic residue modulo 
    a prime p, -1 if it's a non-residue, or 0 if it is zero.
    """
    assert type(a) is int
    if a % p == 0:
        return 0
    else:
        return 1 if _eulers_criterion(a, p) else -1


def _tonelli_shanks(a: int, p: int) -> tuple[int, int]:
    """
    Tonelli-Shanks algorithm solves x^2 = a mod p where p is prime. a must be a 
    quadratic residue modulo p. Returns both solutions in a tuple -- the even one 
    followed by the odd one.
    https://en.wikipedia.org/wiki/Tonelli%E2%80%93Shanks_algorithm
    """
    def even_first(x1, x2):
        return (x1, x2) if x1 % 2 == 0 else (x2, x1)
    
    assert _legendre_symbol(a, p) >= 0

    if a % p == 0:
        return 0, p
    if _congruent(p, 3, 4):
        y1 = _mod_exp(a, (p + 1) >> 2, p)
        return even_first(y1, p - y1)
    q = p - 1
    s = 0
    while q % 2 == 0:
        s += 1
        q >>= 1
     
    # Find a QNR
    z = 2
    while _legendre_symbol(z, p) >= 0:
        z += 1
    
    m = s
    c = _mod_exp(z, q, p)
    t = _mod_exp(a, q, p)
    r = _mod_exp(a, (q + 1) >> 1, p)

    while (t % p) != 1:
        for i in range(0, m):
            if _mod_exp(t, 2 ** i, p) == 1:
                break
        b = _mod_exp(c, (2 ** (m - i - 1)), p)
        m = i
        c = _mod_exp(b, 2, p)
        t = t * _mod_exp(b, 2, p)
        r = (r * b) % p
    
    return even_first(r, p - r)


def secp256k1_random_scalar() -> int:
    return 1 + (uint256_random() % (SECP256K1_ORDER - 2))


def secp256k1_add(point_p: tuple[int, int], point_q: tuple[int, int]) -> tuple[int, int]:
    """Add two points P and Q resulting in point R."""
    px, py = point_p
    qx, qy = point_q

    if point_p == POINT_AT_INFINITY:
        rx, ry = point_q
    elif point_q == POINT_AT_INFINITY:
        rx, ry = point_p
    elif px == qx:
        if py == qy:
            # Point doubling.
            s = (((3 * px**2) + SECP256K1_A) * _mmi(2 * py, SECP256K1_P)) % SECP256K1_P
            rx = (s**2 - (2 * px)) % SECP256K1_P
            ry = ((s * (px - rx)) - py) % SECP256K1_P
        else:
            # Opposite points.
            rx, ry = POINT_AT_INFINITY
    else:
        # Point addition.
        s = ((qy - py) * _mmi(qx - px, SECP256K1_P)) % SECP256K1_P
        rx = (s**2 - px - qx) % SECP256K1_P
        ry = ((s * (px - rx)) - py) % SECP256K1_P
    return rx, ry


def secp256k1_multiply(scalar: int, point: tuple[int, int] = SECP256K1_GENERATOR) -> tuple[int, int]:
    """Multiply point by scalar where scalar >= 0."""
    if scalar == 0:
        return POINT_AT_INFINITY
    elif scalar == 1:
        return point
    elif scalar == 2:
        return secp256k1_add(point, point)
    elif scalar % 2 == 1:
        return secp256k1_add(point, secp256k1_multiply(scalar - 1, point))
    else:
        return secp256k1_multiply(2, secp256k1_multiply(scalar >> 1, point))


def secp256k1_compute_ys(x: int) -> tuple[int, int]:
    """Compute the two y co-ordinates given an x coordinate. Even first."""
    return _tonelli_shanks((_mod_exp(x, 3, SECP256K1_P) + SECP256K1_A * x + SECP256K1_B) % SECP256K1_P, SECP256K1_P)
