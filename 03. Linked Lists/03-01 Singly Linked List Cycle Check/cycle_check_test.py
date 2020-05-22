import unittest

from cycle_check import cycle_check, Node


class CycleCheckTest(unittest.TestCase):
    def test(self):
        # CREATE CYCLE LIST
        a = Node(1)
        b = Node(2)
        c = Node(3)

        a.nextnode = b
        b.nextnode = c
        c.nextnode = a  # Cycle Here!

        # CREATE NON CYCLE LIST
        x = Node(1)
        y = Node(2)
        z = Node(3)

        x.nextnode = y
        y.nextnode = z

        self.assertEqual(cycle_check(a), True)
        self.assertEqual(cycle_check(x), False)
