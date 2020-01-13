from collections import deque


class Stack:

    def __init__(self):
        self.items = deque()

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if not len(self.items):
            return self.items.pop()

    def top(self):
        return self.items[-1]

    def empty(self):
        return len(self.items) == 0


class MyQueue:

    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def push(self, x: int) -> None:
        self.s1.push(x)

    def pop(self) -> int:
        if not self.s2.empty():
            return self.s2.pop()
        while not self.s1.empty():
            self.s2.push(self.s1.pop())
        return self.s2.pop()

    def peek(self) -> int:
        if not self.s2.empty():
            return self.s2.top()
        while not self.s1.empty():
            self.s2.push(self.s1.pop())
        return self.s2.top()

    def empty(self) -> bool:
        return self.s1.empty() and self.s2.empty()


class Deque:

    def __init__(self):
        self.items = deque()

    def push(self, val):
        self.items.append(val)

    def pop(self):
        return self.items.pop()

    def top(self):
        return self.items[-1]

    def empty(self):
        return len(self.items) == 0