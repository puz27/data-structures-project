from src.queue import Queue

class Node():
    """Класс для узла односвязного списка"""

    def __init__(self, data: dict, next_node=None, prev_node=None):
        """
        Конструктор класса Node
        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node


class LinkedList(Queue):
    """Класс для односвязного списка"""

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        if self.head is None:
            self.tail = Node(data)
            self.head = self.tail
        else:
            self.head.prev_node = Node(data)
            self.head.prev_node.next_node = self.head
            self.head = self.head.prev_node

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        if self.tail is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next_node = Node(data)
            self.tail.next_node.prev_node = self.tail
            self.tail = self.tail.next_node

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next_node

        ll_string += ' None'
        return ll_string
