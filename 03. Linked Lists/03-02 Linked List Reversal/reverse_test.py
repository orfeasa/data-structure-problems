import unittest

from reverse import reverse, Node


class ReverseTest(unittest.TestCase):
    def test(self):
        # Create a list of 4 nodes
        a = Node(1)
        b = Node(2)
        c = Node(3)
        d = Node(4)

        # Set up order a,b,c,d with values 1,2,3,4
        a.nextnode = b
        b.nextnode = c
        c.nextnode = d

        # Now let's check the values of the nodes coming after a, b and c
        self.assertEqual(a.nextnode.value, 2)
        self.assertEqual(b.nextnode.value, 3)
        self.assertEqual(c.nextnode.value, 4)

        # catch AttributeError exception
        self.assertRaises(AttributeError, lambda: d.nextnode.value)

        reverse(a)
        self.assertEqual(d.nextnode.value, 3)
        self.assertEqual(c.nextnode.value, 2)
        self.assertEqual(b.nextnode.value, 1)

        # a.nextnode.value
        # catch AttributeError exception
        self.assertRaises(AttributeError, lambda: a.nextnode.value)
