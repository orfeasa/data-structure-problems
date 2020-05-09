import unittest

from anagram import anagram


class AnagramTest(unittest.TestCase):
    def test_spaces(self):
        self.assertEqual(anagram("go go go", "gggooo"), True)

    def test_chars_only(self):
        self.assertEqual(anagram("abc", "cba"), True)

    def test_multiple_spaces(self):
        self.assertEqual(anagram("hi man", "hi     man"), True)

    def test_repetition(self):
        self.assertEqual(anagram("aabbcc", "aabbc"), False)

    def test_fail(self):
        self.assertEqual(anagram("123", "1 2"), False)
