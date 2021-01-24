from litcoin.mnemonic import entropy_to_wordlist, wordlist_to_entropy
from litcoin.binhex import b
import unittest

ENTROPY_128 = b("5e2d74684bdf866fe46730a2a4870b59")
ENTROPY_160 = b("df78098bac97dfa51908642cbb78fed901716aa8")
ENTROPY_192 = b("9876dad7628b980d89c6ba628967cbda67289078651876d9")
ENTROPY_224 = b("000837165cbda6829786bd78490273098700091876bcdae789deee80")
ENTROPY_256 = b("000000000476cbbbad72978639890707aaabc098708707d234908fee28760092")

WORDLIST_128 = [
    "funny", "hill", "borrow", "nut",
    "wear", "dawn", "muscle", "toward",
    "pencil", "category", "security", "recall"
]

WORDLIST_160 = [
    "term", "scare", "glass", "float", "law",
    "spoon", "goddess", "arrive", "coach", "swift",
    "distance", "rare", "blade", "relief", "patrol"
]

WORDLIST_192 = [
    "observe", "replace", "remind", "shallow", "ridge", "almost",
    "check", "struggle", "glad", "enroll", "very", "regular",
    "income", "else", "thunder", "perfect", "item", "sniff"
]

WORDLIST_224 = [
    "abandon", "double", "sheriff", "ride", "surprise", "donor", "fun",
    "stumble", "joke", "elite", "orphan", "basic", "hybrid", "afraid",
    "gift", "stuff", "sustain", "detail", "jeans", "tackle", "assume"
]

WORDLIST_256 = [
    "abandon", "abandon", "abandon", "angry", "hole", "tape", "remind", "fancy",
    "mail", "slush", "dove", "aunt", "primary", "theory", "gift", "axis",
    "amazing", "museum", "category", "cabin", "tip", "deposit", "across", "exact"
]


class TestMnemonic(unittest.TestCase):
    def test_entropy_to_wordlist(self):
        self.assertEqual(entropy_to_wordlist(ENTROPY_128), WORDLIST_128)
        self.assertEqual(entropy_to_wordlist(ENTROPY_160), WORDLIST_160)
        self.assertEqual(entropy_to_wordlist(ENTROPY_192), WORDLIST_192)
        self.assertEqual(entropy_to_wordlist(ENTROPY_224), WORDLIST_224)
        self.assertEqual(entropy_to_wordlist(ENTROPY_256), WORDLIST_256)

    def test_wordlist_to_entropy(self):
        self.assertEqual(wordlist_to_entropy(WORDLIST_128), ENTROPY_128)
        self.assertEqual(wordlist_to_entropy(WORDLIST_160), ENTROPY_160)
        self.assertEqual(wordlist_to_entropy(WORDLIST_192), ENTROPY_192)
        self.assertEqual(wordlist_to_entropy(WORDLIST_224), ENTROPY_224)
        self.assertEqual(wordlist_to_entropy(WORDLIST_256), ENTROPY_256)