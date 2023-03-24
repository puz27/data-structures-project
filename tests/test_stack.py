import unittest
from src.stack import Node, Stack


class Test(unittest.TestCase):

    def test_Node_1(self):
        """Проверка создания экземпляра класса Node"""
        n1 = Node(999, None)
        self.assertEqual(n1.data, 999)

    def test_Node_2(self):
        """Проверка возможности добавления ссылки на следующий элемент"""
        n1 = Node(999, 1000)
        self.assertEqual(n1.next_node, 1000)

    def test_Node_3(self):
        """Проверка верхнего элемента в стеке"""
        stack = Stack()
        stack.push("datas")
        stack.push("datas_2")
        self.assertEqual(stack.top.data, "datas_2")

    def test_Node_4(self):
        """Проверка верхнего элемента в стеке после удаления"""
        stack = Stack()
        stack.push("datas")
        stack.push("datas_2")
        stack.pop()
        self.assertEqual(stack.top.data, "datas")

    def test_Node_5(self):
        """Проверка вывода данныз стека через str"""
        stack = Stack()
        stack.push('data')
        self.assertEqual(str(stack), str(["data"]))
