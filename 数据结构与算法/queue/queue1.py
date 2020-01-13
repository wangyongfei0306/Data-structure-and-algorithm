class Deque:
    def __init__(self):
        self.queue = []

    def push(self, value):
        self.queue.append(value)

    def pop(self):
        if not self.empty():
            return self.queue.pop(0)

    def empty(self):
        return self.length() == 0

    def length(self):
        return len(self.queue)

    def print_result(self):
        print(self.queue)


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.empty():
            return self.stack.pop(-1)

    def empty(self):
        return self.length() == 0

    def length(self):
        return len(self.stack)


class Solution:
    def __init__(self):
        self.maxSize = 7

    @staticmethod
    def create_queue(list_a):
        queue1 = Deque()
        for i in list_a:
            queue1.push(i)
        return queue1

    @staticmethod
    def result1(queue1):
        """ 找到队列中最小的值，并返回它的索引 """
        n = queue1.length()  # 取得队列的元素数
        k = queue1.pop()  # 规定第一个元素作为最小的，保存在k中
        queue1.push(k)  # 再把退出来的元素推入进去
        i = 0
        j = 1
        while j < n:
            x = queue1.pop()
            if x < k:
                k = x
                i = j
            queue1.push(x)
            j += 1
        print(n, i, k)

    @staticmethod
    def result2(data):
        """
        :param data:原队列
        :return: 返回逆序后的队列
        """
        stack = Stack()
        while not data.empty():  # 如果原队列不为空
            stack.push(data.pop())  # 将原队列的元素退出来压入到栈中
        while not stack.empty():  # 如果栈不为空
            data.push(stack.pop())  # 弹出栈的栈顶元素，推入队列中
        return data  # 返回队列对象

    def result3(self, queue1, data):
        if queue1.length == self.maxSize:
            return 0
        queue1.push(data)
        return queue1


if __name__ == '__main__':
    solution = Solution()
    list_a = [5, 2, 6, 1, 3, 4]
    queue = solution.create_queue(list_a)  # 创造的队列对象
    print('创建的队列：', queue.queue)
    # print(solution.create_queue(list_a))
    print(solution.result2(queue).queue)
    pass

