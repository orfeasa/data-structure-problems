import unittest

from permute import permute


class PermuteTest(unittest.TestCase):
    def test(self):
        self.assertEqual(
            sorted(permute("dog")), sorted(["dog", "dgo", "odg", "ogd", "gdo", "god"])
        )
        self.assertEqual(
            sorted(permute("abc")), sorted(["abc", "acb", "bac", "bca", "cab", "cba"])
        )
