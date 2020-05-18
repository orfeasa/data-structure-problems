import unittest

from deque import Deque


class DequeTest(unittest.TestCase):
    def test1(self):
        deq = Deque()

        self.assertEqual(deq.size(), 0)

        deq.add_front(2)
        deq.add_front(1)
        deq.add_rear(3)

        self.assertEqual(deq.remove_front(), 1)
        self.assertEqual(deq.is_empty(), False)
        self.assertEqual(deq.remove_rear(), 3)
        self.assertEqual(deq.remove_rear(), 2)
        self.assertEqual(deq.is_empty(), True)
