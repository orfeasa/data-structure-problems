import unittest

from queue import Queue


class QueueTest(unittest.TestCase):
    def test1(self):
        q = Queue()
        self.assertEqual(q.is_empty(), True)

        q.enqueue(1)
        q.enqueue("two")
        q.enqueue(3)

        self.assertEqual(q.size(), 3)
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.dequeue(), "two")
        self.assertEqual(q.is_empty(), False)
        self.assertEqual(q.dequeue(), 3)
        self.assertEqual(q.is_empty(), True)
