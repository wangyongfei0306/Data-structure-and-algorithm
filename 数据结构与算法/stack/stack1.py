from 数据结构与算法.table import MyLinkList


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.empty():
            return False
        return self.stack.pop(-1)

    def top(self):
        if self.empty():
            return None
        return self.stack[-1]

    def empty(self):
        return len(self.stack) == 0


class Solution:
    def __init__(self):
        self.stack = Stack()

    def result1(self, head):
        p = head.next  # 首元结点
        print(p.data)
        while p:
            self.stack.push(p.data)
            p = p.next
        print(self.stack)
        p = head.next  # 再赋值一次用来遍历
        while p:
            x = self.stack.pop()
            if p.data != x:
                return False
            else:
                p = p.next
        return True

    def result2(self, head):
        pre = head
        p = head.next
        while p:
            pre.next = p.next
            self.stack.push(p)
            pre = p
            p = p.next
        p = head
        while not self.stack.empty():
            x = self.stack.pop()
            p.next = x
            p = p.next
        p.next = None
        return head


if __name__ == '__main__':
    list_a = [1, 3, 4, 6, 7, 9]
    link = MyLinkList()
    head = link.create(list_a)

    solution = Solution()
    # print(solution.result1(head))
    link.print_link(solution.result2(head))