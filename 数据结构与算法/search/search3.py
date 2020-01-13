import math


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class MyLinkList:
    def __init__(self):
        self.head = Node(-1)

    def create(self, l):
        rear = self.head
        for i in range(len(l)):
            rear.next = Node(l[i])
            rear = rear.next
        rear.next = None
        self.print_link(self.head)
        return self.head

    @staticmethod
    def print_link(head_):
        """
        :param head_:头结点
        :return: 打印链表
        """
        res = []
        p = head_.next
        while p:
            res.append(str(p.data))
            p = p.next
        print('->'.join(res))

    def m_search(self, h1, h2):
        """ 找两个等长的有序单链表的中位数 """
        p1, p2, n = h1, h2, 0
        while p1.next:
            n += 1
            p1 = p1.next
        p1, k, v = h1, 0, 0
        while k < n:
            if p1.data < p2.data:
                v = p2.data
                p1 = p1.next
            else:
                v = p1.data
                p2 = p2.next
            k += 1
        return v

    def bin_search(self, l, x):
        left, right, m = 0, len(l) - 1, 0
        while left <= right:
            m = (left + right) // 2
            if l[m] == x:
                break
            elif l[m] < x:
                left = m + 1
            else:
                right = m - 1
        if x == l[m]:
            return m
        elif left < len(l) - 1 and right >= 0:
            return left
        else:
            return -1

    def search_subarea(self, l, s, x):
        """ 把数组等分成s个子区间，不建立索引表进行顺序分区查找 """
        n = len(l)
        d = math.ceil(n/s) if n%s != 0 else n//s
        i = 0
        while i < d * (s - 1) and l[i+d-1] < x:
            i = i + d
        low = i
        high = i + d - 1
        if i == d * (s - 1):
            high = n - 1
        while low <= high:
            mid = (low + high) // 2
            if l[mid] == x:
                return mid
            elif l[mid] > x:
                high = mid - 1
            else:
                low = mid + 1
        return -1


if __name__ == '__main__':
    list_a = [1, 3, 4, 6, 7, 9]
    list_b = [11, 13, 15, 16, 19]
    list_c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    link1 = MyLinkList()
    # link2 = MyLinkList()
    # head1 = link1.create(list_a)
    # head2 = link2.create(list_b)

    # print(link1.m_search(head1, head2))
    # print(link1.bin_search(list_a, 5))
    print(link1.search_subarea(list_c, 3, 8))

