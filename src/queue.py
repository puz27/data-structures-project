class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node=None, prev_node=None) -> None:
        """
        Конструктор класса Node
        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node

    def __repr__(self) -> str:
        return f"{self.data}"


class Queue:
    """Класс для очереди"""

    def __init__(self) -> None:
        """Конструктор класса Queue"""
        self.head = None
        self.tail = None

    def enqueue(self, data: str) -> None:
        """
        Метод для добавления элемента в очередь
        :param data: данные, которые будут добавлены в очередь
        """

        if self.tail is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next_node = Node(data)
            self.tail.next_node.prev_node = self.tail
            self.tail = self.tail.next_node

    def dequeue(self) -> str:
        """
        Метод для удаления элемента из очереди и его возвращения
        :return: данные удаленного элемента
        """
        if self.head and self.tail is not None:
            old_head = self.head
            if self.head.next_node is not None:
                new_head = self.head.next_node
                del self.head
                self.head = new_head
                self.head.prev_node = None
                return old_head.data
            else:
                self.head = None
                self.tail = None
                return old_head.data

    def __str__(self) -> str:
        """Магический метод для строкового представления объекта
        :return: Вывод строкового представления в виде данных очереди
        """
        show_queue = []
        last_item = self.tail

        while last_item is not None:
            show_queue.append(last_item.data + "\n")
            last_item = last_item.prev_node
        show_queue.reverse()
        return f"{''.join(show_queue).rstrip()}"
