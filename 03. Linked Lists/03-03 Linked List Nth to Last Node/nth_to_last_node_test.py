import unittest

from nth_to_last_node import nth_to_last_node, Node


class NthToLastNodeTest(unittest.TestCase):
    def test(self):
        # Create a list of 5 nodes
        a = Node(1)
        b = Node(2)
        c = Node(3)
        d = Node(4)
        e = Node(5)

        # Set up order a,b,c,d,e with values 1,2,3,4,5
        a.nextnode = b
        b.nextnode = c
        c.nextnode = d
        d.nextnode = e

        # This would return the node d with a value of 4, because its the 2nd to last node.
        target_node = nth_to_last_node(2, a)

        self.assertEqual(target_node.value, 4)
