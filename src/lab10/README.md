
# GooDy-PiraTe (Саргаева Анна БИВТ-25-1)

## Лабораторная работа 10

### Задание A
structures.py
```python
from collections import deque


class Stack:
    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        try:
            return self._data.pop()
        except IndexError:
            raise ValueError("Стек пуст")

    def peek(self):
        try:
            return self._data[-1]
        except IndexError:
            return None

    def is_empty(self) -> bool:
        return not self._data


class Queue:
    def __init__(self):
        self._data = deque()

    def enqueue(self, item):
        self._data.append(item)

    def dequeue(self):
        try:
            return self._data.popleft()
        except IndexError:
            raise ValueError("Очередь пуста")

    def peek(self):
        try:
            return self._data[0]
        except IndexError:
            return None

    def is_empty(self) -> bool:
        return not self._data

```
![Картинка 1](./screenshots/stack.png)
![Картинка 2](./screenshots/queue.png)
### Задание B
linked_list.py
```python
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self._size += 1

    def prepend(self, value):
        new_node = Node(value, next=self.head)
        self.head = new_node
        self._size += 1

    def insert(self, idx, value):
        if idx < 0:
            raise IndexError("negative index is not supported")
        if idx > self._size:
            raise IndexError("index is out of range")
        if idx == 0:
            self.prepend(value)
            return
        current = self.head
        for _ in range(idx - 1):
            current = current.next
        new_node = Node(value, next=current.next)
        current.next = new_node
        self._size += 1

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.value
            current = current.next

    def __len__(self):
        return self._size

    def __repr__(self):
        values = list(self)
        return f"SinglyLinkedList({values})"

```
![Картинка 3](./screenshots/sll.png)
