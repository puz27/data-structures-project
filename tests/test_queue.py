import unittest
from src.queue import Node, Queue

class Test(unittest.TestCase):

    def test_Node_1(self):
        n1 = Node(999, None)
        self.assertEqual(n1.data, 999)

    def test_Node_2(self):
        n1 = Node(1500, 2000)
        self.assertEqual(n1.next_node, 2000)

    def test_Queue_1(self):
        queue = Queue()
        queue.enqueue('data5')
        queue.enqueue('data6')
        self.assertEqual(str(queue), 'data5\ndata6')

    def test_Queue_2(self):
        queue = Queue()
        queue.enqueue('data7')
        queue.enqueue('data8')
        queue.dequeue()
        self.assertEqual(str(queue), 'data8')

    def test_Queue_3(self):
        queue = Queue()
        queue.enqueue('data7')
        queue.enqueue('data8')
        queue.dequeue()
        queue.dequeue()
        self.assertEqual(str(queue), '')

    def test_Queue_4(self):
        queue = Queue()
        queue.enqueue('data7')
        queue.enqueue('data8')
        self.assertEqual(queue.dequeue(), 'data7')

    def test_Queue_5(self):
        queue = Queue()
        queue.enqueue('data7')
        queue.dequeue()
        self.assertEqual(queue.dequeue(), None)