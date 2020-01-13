from collections import deque


class Node:
    def __init__(self, data=None, left=None, right=None, count=1):
        self.data = data
        self.right = right
        self.left = left
        self.count = count


class Start:
    def __init__(self, string):
        self.string = string
        self.root = None
        self.lr = True
        self.queue = deque()

    def create_tree_pre_in(self, post_ord, in_ord):
        """
        :param post_ord: 后序遍历结果
        :param in_ord: 中序遍历结果
        :return: 构建树的根结点
        """
        if len(in_ord) == 0:
            return None
        root = Node(post_ord[-1])
        mid = in_ord.index(post_ord[-1])
        root.left = self.create_tree_pre_in(post_ord[:mid], in_ord[:mid])
        root.right = self.create_tree_pre_in(post_ord[mid:len(post_ord)-1], in_ord[mid+1:])
        return root

    def pre_ord(self, root):
        if root:
            print(root.data, end=' ')
            self.pre_ord(root.left)
            self.pre_ord(root.right)

    def in_ord(self, root):
        if root:
            self.in_ord(root.left)
            print(root.data, end=' ')
            self.in_ord(root.right)

    def special_in_ord(self, root):
        if root:
            self.in_ord(root.left)
            print(root.data, ":", root.count, end=', ')
            self.in_ord(root.right)

    def print_by_zigzag(self, t):
        """ 实现二叉树的zigzag打印 """
        self.queue.append(t)
        last, s = t, None
        while len(self.queue) != 0:
            if self.lr:                             # 从左向右
                p = self.queue.popleft()            # 从左端 pop
                if p.left:                          # 存在左子树
                    s = p.left if not s else s      # 标识为每一层的最左结点，用来改变打印方向
                    self.queue.append(p.left)       # 结点的左子树根结点从队列的右边进队
                if p.right:                         # 存在右子树
                    s = p.right if not s else s     # 标识为每一层的最右结点，用来改变打印方向
                    self.queue.append(p.right)      # 结点的右子树根结点从队列的右边进队
            else:                                   # 从右向左
                p = self.queue.pop()                # 从右端 pop
                if p.right:                         # 存在右子树
                    s = p.right if not s else s     # 标识为每一层的最右结点，用来改变打印方向
                    self.queue.appendleft(p.right)  # 结点的右子树根结点从队列的左边进队
                if p.left:                          # 存在左子树
                    s = p.left if not s else s      # 标识为每一层的最左结点，用来改变打印方向
                    self.queue.appendleft(p.left)   # 结点的左子树根结点从队列的左边进队
            print(p.data, end=' ')                  # 打印结点值
            if p == last and len(self.queue) != 0:  # 如果当前结点是每一层的标识性结点且队列不为空
                self.lr = not self.lr               # 改变打印方向
                last = s                            # 改变标识位
                s = None
                print('\n')
        print('\n')

    def comeback(self, low, high, l):
        """ 根据先序遍历恢复二叉查找树 """
        if low > high:
            return None
        else:
            t = Node(l[low])
            i = low + 1
            while i <= high:
                if l[i] > l[low]:
                    break
                i += 1
            t.left = self.comeback(low + 1, i - 1, l)
            t.right = self.comeback(i, high, l)
            return t

    @staticmethod
    def level(t, p):
        """ 查找指定结点的值所在二叉查找树的层次 """
        k = 0
        if t:
            k = k + 1
            while t.data != p and t:
                if t.data > p:
                    t = t.left
                else:
                    t = t.right
                k = k + 1
            if t:
                return k
            return -1

    def insert_x(self, t, x):
        """ 向二叉查找树中插入一个元素 """
        if not t:
            t = Node(x)
            return t
        elif x == t.data:
            pass
        elif x < t.data:
            t.left = self.insert_x(t.left, x)
        else:
            t.right = self.insert_x(t.right, x)
        return t

    def remove_max(self, t):
        """ 二叉树中查找最大的元素并删除 """
        if not t:
            return False
        pre, p = None, t
        while p.right:
            pre = p
            p = p.right
        if not pre:
            p = p.left
        else:
            pre.right = p.left
        return t

    def create_best_tree(self, low, high, l):
        """ 按什么方式生成二叉查找树平衡性最好而且方法又简单 """
        if low > high:
            return None
        else:
            mid = (low + high) // 2
            t = Node(l[mid])
            t.left = self.create_best_tree(low, mid - 1, l)
            t.right = self.create_best_tree(mid + 1, high, l)
            return t

    def insert1(self, t, x):
        """ 查找x如果有则count加1，否则作为新结点插入 """
        p, pre = t, None
        while p:
            if p.data == x:
                p.count += 1
                return t
            else:
                pre = p
                p = p.left if x < p.data else p.right
        s = Node(x)
        if not pre:  # 如果经过while循环则pre肯定不为空，如果pre为空则代表着根结点不存在
            t = s
        elif x > pre.data:
            pre.right = s
        else:
            pre.left = s
        return t


if __name__ == '__main__':
    begin = Start('')
    post_ord = [15, 20, 7, 6, 9, 3]
    in_ord = [15, 7, 20, 3, 6, 9]
    t = begin.create_tree_pre_in(post_ord, in_ord)

    # begin.pre_ord(t)

    # begin.print_by_zigzag(t)

    # h = begin.comeback(0, 8, [40, 20, 10, 30, 70, 50, 60, 90, 80])
    # h = begin.comeback(0, 4, [40, 20, 10, 30, 50])
    h = begin.comeback(0, 0, [1])

    # print(begin.level(h, 30))
    # begin.in_ord(h)
    # print('---------')
    # begin.in_ord(begin.insert_x(h, 40))
    # t2 = begin.remove_max(h)
    # print(t2)
    # begin.in_ord(t2)

    # t3 = begin.create_best_tree(0, 10, [7, 12, 13, 15, 21, 33, 38, 41, 49, 55, 58])
    # begin.in_ord(t3)

    t4 = begin.insert1(h, 50)
    begin.special_in_ord(t4)
