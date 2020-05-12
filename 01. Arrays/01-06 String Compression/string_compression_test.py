import unittest

from string_compression import compress


class CompressionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(compress(""), "")
        self.assertEqual(compress("AABBCC"), "A2B2C2")
        self.assertEqual(compress("AAABCCDDDDD"), "A3B1C2D5")
