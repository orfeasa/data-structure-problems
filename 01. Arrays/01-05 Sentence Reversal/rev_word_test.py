import unittest

from rev_word import rev_word


class FinderTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(rev_word("    space before"), "before space")
        self.assertEqual(rev_word("space after     "), "after space")
        self.assertEqual(
            rev_word("   Hello John    how are you   "), "you are how John Hello"
        )
        self.assertEqual(rev_word("1"), "1")
