class Deque:
    def __init__(self):
        self.maxSize = 7
        self.front = 0
        self.rear = 0
        self.queue = [None] * self.maxSize
        self.length = self.length_()  # 对应的元素非None

    def push(self, value):
        if self.length < self.maxSize:
            pass

    def pop(self):
        if self.length > 0:
            x = self.queue[0]

    def length_(self):
        count = 0
        for i in self.queue:
            if i is not None:
                count += 1
        return count


class Solution:
    def __init__(self):
        self.maxSize = 7
        self.front = 0
        self.rear = 0

    def create_deque(self, nums):
        pass


if __name__ == '__main__':
    deque = Deque()
    print(deque.queue)
    print(deque.length)