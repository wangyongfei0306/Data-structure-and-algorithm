class ListNode:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = ListNode(-1)
        self.length = 0

    def add(self, value):
        new = ListNode(value)
        if self.head.next:
            p = self.head
            while p.next:
                p = p.next
            p.next = new
        else:
            self.head.next = new
        self.length += 1


def main():
    llist = LinkedList()
    llist.add(1)
    llist.add(2)
    llist.add(3)
    print('---------------')
    # 头节点的下一个也就是第一个节点 p1
    p1 = llist.head.next
    # 放进节点
    jiedian = []
    while p1:
        # 把节点放进列表
        jiedian.append(str(p1.value))
        p1 = p1.next
    print(jiedian)
    print('->'.join(jiedian))


if __name__ == '__main__':
    main()