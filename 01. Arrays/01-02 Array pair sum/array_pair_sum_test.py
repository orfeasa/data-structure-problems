import unittest

from array_pair_sum import pair_sum


class ArrayPairSumTest(unittest.TestCase):
    def test(self):
        self.assertEqual(
            pair_sum([1, 9, 2, 8, 3, 7, 4, 6, 5, 5, 13, 14, 11, 13, -1], 10), 6
        )
        self.assertEqual(pair_sum([1, 2, 3, 1], 3), 1)
        self.assertEqual(pair_sum([1, 3, 2, 2], 4), 2)
