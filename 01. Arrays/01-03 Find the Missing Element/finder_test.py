import unittest

from finder import finder


class FinderTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(finder([5, 5, 7, 7], [5, 7, 7]), 5)

    def test2(self):
        self.assertEqual(finder([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6]), 5)

    def test3(self):
        self.assertEqual(
            finder([9, 8, 7, 6, 5, 4, 3, 2, 1], [9, 8, 7, 5, 4, 3, 2, 1]), 6
        )
