import unittest

from queue_2_stacks import Queue2Stacks


class Queue2StacksTest(unittest.TestCase):
    def test(self):
        q = Queue2Stacks()
        for i in range(5):
            q.enqueue(i)
        for i in range(5):
            self.assertEqual(q.dequeue(), i)
