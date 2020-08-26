import unittest

from rec_coin import rec_coin


class RecCoinTest(unittest.TestCase):
    def test_rec_coin(self):
        coins = [1, 5, 10, 25]
        self.assertEqual(rec_coin(45, coins), 3)
        self.assertEqual(rec_coin(23, coins), 5)
        self.assertEqual(rec_coin(74, coins), 8)

    def test_non_canonical(self):
        coins = [1, 3, 4, 6]
        self.assertEqual(rec_coin(6, coins), 2)
