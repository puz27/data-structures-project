import unittest
from src.linked_list import LinkedList, Node

class Test(unittest.TestCase):

    def test_Node_1(self):
        n1 = Node(999, None)
        self.assertEqual(n1.data, 999)

    def test_Node_2(self):
        n1 = Node(1500, 2000)
        self.assertEqual(n1.next_node, 2000)