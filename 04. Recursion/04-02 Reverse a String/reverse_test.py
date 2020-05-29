import unittest

from reverse import reverse


class ReverseTest(unittest.TestCase):
    def test(self):
        self.assertEqual(reverse("hello"), "olleh")
        self.assertEqual(reverse("hello world"), "dlrow olleh")
        self.assertEqual(reverse("123456789"), "987654321")
