import unittest

from fibonacci import fib_rec, fib_dyn, fib_iter


class FibonacciTest(unittest.TestCase):
    def test_rec(self):
        self.assertEqual(fib_rec(10), 55)
        self.assertEqual(fib_rec(1), 1)
        self.assertEqual(fib_rec(23), 28657)

    def test_dyn(self):
        self.assertEqual(fib_dyn(10), 55)
        self.assertEqual(fib_dyn(1), 1)
        self.assertEqual(fib_dyn(23), 28657)

    def test_iter(self):
        self.assertEqual(fib_iter(10), 55)
        self.assertEqual(fib_iter(1), 1)
        self.assertEqual(fib_iter(23), 28657)
