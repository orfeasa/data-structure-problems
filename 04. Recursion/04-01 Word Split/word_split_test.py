import unittest

from word_split import word_split


class WordSplitTest(unittest.TestCase):
    def test(self):
        self.assertEqual(
            word_split("themanran", ["the", "ran", "man"]), ["the", "man", "ran"]
        )
        self.assertEqual(
            word_split(
                "ilovedogsJohn", ["i", "am", "a", "dogs", "lover", "love", "John"]
            ),
            ["i", "love", "dogs", "John"],
        )
        self.assertEqual(word_split("themanran", ["clown", "ran", "man"]), [])
