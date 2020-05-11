import unittest

from large_cont_sum import large_cont_sum


class FinderTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(large_cont_sum([1, 2, -1, 3, 4, -1]), 9)

    def test2(self):
        self.assertEqual(large_cont_sum([1, 2, -1, 3, 4, 10, 10, -10, -1]), 29)

    def test3(self):
        self.assertEqual(large_cont_sum([-1, 1]), 1)
