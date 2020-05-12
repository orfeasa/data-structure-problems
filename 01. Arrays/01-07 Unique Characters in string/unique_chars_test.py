import unittest

from unique_chars import uni_char


class UniqueCharTest(unittest.TestCase):
    def test(self):
        self.assertEqual(uni_char(""), True)
        self.assertEqual(uni_char("goo"), False)
        self.assertEqual(uni_char("abcdefg"), True)
