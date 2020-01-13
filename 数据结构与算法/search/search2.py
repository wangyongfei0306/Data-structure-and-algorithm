class Node:
    def __init__(self, data):
        self.data = data
        self.r_link = None
        self.l_link = None


class MyLinked:
    def __init__(self, l=None):
        self.l = l

    def create1(self):
        """ 创建双端链表 """
        l = [1, 3, 5, 7, 9]
        head = Node(-1)
        p = head
        for i in self.l:
            node = Node(i)
            p.r_link = node
            node.l_link = p
            p = p.r_link
        p.r_link = None
        self.print_link(head)
        return head

    def print_link(self, head):
        res = []
        p = head.r_link
        while p:
            res.append(str(p.data))
            p = p.r_link
        print('<-->'.join(res))

    def search1(self, head, x):
        current = head.r_link.r_link.r_link  # 检测指针,总是指向最后成功查找到的结点
        print(current, current.data)
        q = current
        if x < q.data:
            while q and q.data > x:
                q = q.l_link
        else:
            while q and q.data < x:
                q = q.r_link
        if q and q.data == x:
            current = q
            print(current.data)
            return 1
        else:
            return 0


if __name__ == '__main__':
    link = MyLinked([5, 1, 3, 4, 2])
    head = link.create1()

    # print(link.search1(head, 3))
    print(head.r_link.r_link.data)
