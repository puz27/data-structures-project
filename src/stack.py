class Node:
    """Класс для узла стека"""

    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Stack:
    """Класс для стека"""


    def __init__(self):
        """Конструктор класса Stack"""
        self.top = None
        self.stack_data = []


    def push(self, data):
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """
        new_node = Node(data)
        self.stack_data.append(data)
        if self.top:
            new_node.next_node = self.top
        self.top = new_node


    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """
        return self.stack_data.pop()


    def get_stack_data(self):
        """
        Показать данные в стеке
        :return: вызвращает данные в стеке
        """
        return " ".join(self.stack_data)
