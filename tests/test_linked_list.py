import unittest
from src.linked_list import LinkedList
from unittest.mock import patch
from io import StringIO


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

    def test_linked_list_5(self):
        """Проверка вывода данных нод односвязного списка в список"""
        ll = LinkedList()
        ll.insert_beginning({'id': 2})
        ll.insert_at_end({'id': 9})
        self.assertEqual(ll.to_list(), [{'id': 2}, {'id': 9}])

    def test_linked_list_7(self):
        """Проверка поиска по id"""
        ll = LinkedList()
        ll.insert_beginning({'id': 0, 'username': 'serebro'})
        ll.insert_at_end({'id': 1, 'username': 'lazzy508509'})
        self.assertEqual(ll.get_data_by_id(1), {'id': 1, 'username': 'lazzy508509'})

    def test_linked_list_6(self):
        """Проверка вывода исключения"""
        with self.assertRaises(TypeError, "Данные не являются словарем или в словаре нет id.") as cm:
            ll = LinkedList()
            ll.insert_beginning({'id': 1})
            ll.insert_beginning({'id': 2})
            ll.get_data_by_id(666)
        self.assertEqual(str(cm.exception), "Данные не являются словарем или в словаре нет id.")

    def test_linked_list_8(self):
        with patch('sys.stdout', new=StringIO()) as out:
            ll = LinkedList()
            ll.insert_beginning({'id': 1})
            ll.insert_beginning({'id': 2})
            ll.get_data_by_id(666)
        self.assertEqual(out.getvalue(), "Данные не являются словарем или в словаре нет id.")
