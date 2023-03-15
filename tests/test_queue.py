import unittest
from src.queue import Node, Queue

class Test(unittest.TestCase):

    def test_Node_1(self):
        n1 = Node(999, None)
        self.assertEqual(n1.data, 999)

    def test_Node_2(self):
        n1 = Node(1500, 2000)
        self.assertEqual(n1.next_node, 2000)

    def test_Node_3(self):
        queue = Queue()
        queue.enqueue('data5')
        queue.enqueue('data6')
        self.assertEqual(queue.tail, 'data6')

    def test_Node_4(self):
        queue = Queue()
        queue.enqueue('data7')
        queue.enqueue('data8')
        self.assertEqual(queue.head, 'data7')