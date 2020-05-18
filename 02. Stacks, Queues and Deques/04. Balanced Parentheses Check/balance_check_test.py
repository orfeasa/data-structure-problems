import unittest

from balance_check import balance_check


class BalanceCheckTest(unittest.TestCase):
    def test(self):
        self.assertEqual(balance_check("[]"), True)
        self.assertEqual(balance_check("[](){([[[]]])}"), True)
        self.assertEqual(balance_check("()(){]}"), False)
