import unittest
from src.linked_list import LinkedList, Node

class Test(unittest.TestCase):

    def test_linked_list_1(self):
        """Проверка вывода элементов односвязного списка"""
        ll = LinkedList()
        self.assertEqual(str(ll), "None")

    def test_linked_list_2(self):
        """Проверка добавления элемента в начало односвязного списка"""
        ll = LinkedList()
        ll.insert_beginning({'id': 1})
        self.assertEqual(str(ll), "{'id': 1} -> None")

    def test_linked_list_3(self):
        """Проверка добавления элемента в начало и конец односвязного списка"""
        ll = LinkedList()
        ll.insert_beginning({'id': 1})
        ll.insert_at_end({'id': 10})
        self.assertEqual(str(ll), "{'id': 1} -> {'id': 10} -> None")

    def test_linked_list_4(self):
        """Проверка добавления элементов в начало и конец односвязного списка"""
        ll = LinkedList()
        ll.insert_beginning({'id': 2})
        ll.insert_at_end({'id': 9})
        ll.insert_beginning({'id': 1})
        ll.insert_at_end({'id': 10})
        self.assertEqual(str(ll), "{'id': 1} -> {'id': 2} -> {'id': 9} -> {'id': 10} -> None")

