from litcoin.mnemonic import entropy_to_wordlist, wordlist_to_entropy, wordlist_to_seed
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

WORDLIST_128_WRONG_CHECKSUM = [
    "funny", "hill", "borrow", "nut",
    "wear", "dawn", "muscle", "toward",
    "pencil", "category", "security", "wife"
]

WORDLIST_160_WRONG_CHECKSUM = [
    "term", "scare", "glass", "float", "law",
    "spoon", "goddess", "winner", "coach", "swift",
    "distance", "rare", "blade", "relief", "patrol"
]

WORDLIST_192_WRONG_CHECKSUM = [
    "observe", "replace", "remind", "shallow", "ridge", "almost",
    "check", "struggle", "glad", "enroll", "very", "regular",
    "virtual", "else", "thunder", "perfect", "item", "sniff"
]

WORDLIST_224_WRONG_CHECKSUM = [
    "tuna", "double", "sheriff", "ride", "surprise", "donor", "fun",
    "stumble", "joke", "elite", "orphan", "basic", "hybrid", "afraid",
    "gift", "stuff", "sustain", "detail", "jeans", "tackle", "assume"
]

WORDLIST_256_WRONG_CHECKSUM = [
    "abandon", "abandon", "abandon", "angry", "hole", "tape", "remind", "fancy",
    "mail", "slush", "dove", "aunt", "primary", "theory", "gift", "axis",
    "amazing", "museum", "category", "cabin", "tip", "deposit", "trial", "exact"
]

SEED_128 = b("b0cfd663b005a57e720beecb83345901c80ec9c30851e8e7f08cea3b1cffceb7"
             "5415683f4f7ba469df7eb3fa1b22c9def35ea7c8336760ba5ab0f3dcba98b27f")

SEED_160 = b("4e98441c82065432bb4e2fa571fb9cc0bf080df1bc90302ef56bd55810243f4b"
             "9fa388d837c4da97778e426ad9760470aab8c08acb290247b149ae7c8bdfed3c")

SEED_192 = b("383c29df199a88c94ec2024c1d937a7762962659cc00a09920af5b5e7884cb4a"
             "be4fba3af033d1378b5e67b1f420a3bfe442e1590d4348bd377561903f1d753e")

SEED_224 = b("e1d80aec5438832f0b159d5af0d6c9e9177a3fd88f5b71a7388d075656e3c6b6"
             "2286bddbd4920909f125179bdb26c29c8a7dc3ba60e3e7a15708799fe63c8641")

SEED_256 = b("3d833acb9145d5e7a8321e5edc7ef30f02b28c1709258f7ab0518f3bb5d6da31"
             "693d8e520c56747949675b2563045adcd5366880e1d27fd90aed0700943b9b0c")


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

        with self.assertRaises(AssertionError):
            self.assertEqual(wordlist_to_entropy(WORDLIST_128_WRONG_CHECKSUM), ENTROPY_128)
        with self.assertRaises(AssertionError):
            self.assertEqual(wordlist_to_entropy(WORDLIST_160_WRONG_CHECKSUM), ENTROPY_160)
        with self.assertRaises(AssertionError):
            self.assertEqual(wordlist_to_entropy(WORDLIST_192_WRONG_CHECKSUM), ENTROPY_192)
        with self.assertRaises(AssertionError):
            self.assertEqual(wordlist_to_entropy(WORDLIST_224_WRONG_CHECKSUM), ENTROPY_224)
        with self.assertRaises(AssertionError):
            self.assertEqual(wordlist_to_entropy(WORDLIST_256_WRONG_CHECKSUM), ENTROPY_256)

    def test_wordlist_to_seed(self):
        self.assertEqual(wordlist_to_seed(WORDLIST_128), SEED_128)
        self.assertEqual(wordlist_to_seed(WORDLIST_160), SEED_160)
        self.assertEqual(wordlist_to_seed(WORDLIST_192), SEED_192)
        self.assertEqual(wordlist_to_seed(WORDLIST_224), SEED_224)
        self.assertEqual(wordlist_to_seed(WORDLIST_256), SEED_256)