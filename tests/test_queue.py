import unittest
from src.queue import Node, Queue

class Test(unittest.TestCase):

    def test_Node_1(self):
        """Проверка создания экземпляра класса Node"""
        n1 = Node(999, None)
        self.assertEqual(n1.data, 999)

    def test_Node_2(self):
        """Проверка возможности добавления ссылки на следующий элемент"""
        n1 = Node(1500, 2000)
        self.assertEqual(n1.next_node, 2000)

    def test_Queue_1(self):
        """Проверка добавления элементов в очередь и вывод через str"""
        queue = Queue()
        queue.enqueue('data5')
        queue.enqueue('data6')
        self.assertEqual(str(queue), 'data5\ndata6')

    def test_Queue_2(self):
        """Проверка добавления и удаления элементов в очереди"""
        queue = Queue()
        queue.enqueue('data7')
        queue.enqueue('data8')
        queue.dequeue()
        self.assertEqual(str(queue), 'data8')

    def test_Queue_3(self):
        """Проверка добавления и удаления всех элементов в очереди"""
        queue = Queue()
        queue.enqueue('data7')
        queue.enqueue('data8')
        queue.dequeue()
        queue.dequeue()
        self.assertEqual(str(queue), '')

    def test_Queue_4(self):
        """Проверка, что при удалении метод возвращает удаленный элемент"""
        queue = Queue()
        queue.enqueue('data7')
        queue.enqueue('data8')
        self.assertEqual(queue.dequeue(), 'data7')

    def test_Queue_5(self):
        """Проверка, что при удалении пустой очереди, метод возвращает None"""
        queue = Queue()
        queue.enqueue('data7')
        queue.dequeue()
        self.assertEqual(queue.dequeue(), None)

