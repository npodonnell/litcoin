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


def mmi(a: int, n: int):
    """
    Modular Mulplicative Inverse (MMI) of a mod n. The MMI exists iff
    a and n are coprime.
    """
    assert(n >= 1)
    if a == 1 and n == 1:
        return 0
    else:
        g, x, _ = egcd(a, n)
        if g == 1:
            return x % n
        elif g == -1:
            return mai(x, n)
        else:
            raise ValueError(f"MMI does not exist for {a} modulo {n}")


def secp256k1_add(point_p: tuple[int, int], point_q: tuple[int, int]):
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
            s = (((3 * px**2) + SECP256K1_A) * mmi(2 * py, SECP256K1_P)) % SECP256K1_P
            rx = (s**2 - (2 * px)) % SECP256K1_P
            ry = ((s * (px - rx)) - py) % SECP256K1_P
        else:
            # Opposite points.
            rx, ry = POINT_AT_INFINITY
    else:
        # Point addition.
        s = ((qy - py) * mmi(qx - px, SECP256K1_P)) % SECP256K1_P
        rx = (s**2 - px - qx) % SECP256K1_P
        ry = ((s * (px - rx)) - py) % SECP256K1_P


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
