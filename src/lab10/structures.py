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
