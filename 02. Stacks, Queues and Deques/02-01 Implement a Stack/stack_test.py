import unittest

from stack import Stack


class StackTest(unittest.TestCase):
    def test1(self):
        stack = Stack()

        self.assertEqual(stack.size(), 0)

        stack.push(1)
        stack.push(2)
        stack.push("Three")

        self.assertEqual(stack.pop(), "Three")
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.size(), 1)
        self.assertEqual(stack.is_empty(), False)
        self.assertEqual(stack.peek(), 1)
