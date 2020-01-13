from collections import deque
from 数据结构与算法.stack import ArrayStack


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None
        self.queue = deque()
        self.stack = ArrayStack()
        self.index = 0

    def add(self, data):
        node = TreeNode(data)
        if self.root is None:
            self.root = node
            return
        self.queue.append(self.root)

        while len(self.queue) > 0:
            cur_node = self.queue.popleft()
            if not cur_node.left:
                cur_node.left = node
                return
            else:
                self.queue.append(cur_node.left)
            if not cur_node.right:
                cur_node.right = node
                return
            else:
                self.queue.append(cur_node.right)

    def create_tree(self, pre, s):
        char = pre[s]
        if char == ';':
            return
        if char != '#':
            node = TreeNode(char)
            node_left = TreeNode(pre[2*s+1])
            node_right = TreeNode(pre[2*s+2])
            node.left = node_left
            node.right = node_right
            self.create_tree(pre, s+1)
            self.create_tree(pre, s+2)

    @staticmethod
    def is_empty(p):
        """
        :param p:结点
        :return: 是否为空
        """
        if p is None:
            return True
        else:
            return False

    @staticmethod
    def is_leaf(p):
        """
        :param p:结点
        :return: 是否是叶子结点
        """
        if not p.left and not p.right:
            return True
        else:
            return False

    def height(self, p):
        """
        :param p:结点
        :return: 树的高度
        """
        if not p:
            return 0
        stack = [(1, p)]
        depth = 0
        while stack:
            current_depth, node = stack.pop()
            if node:
                depth = max(depth, current_depth)
                stack.append((current_depth + 1, node.left))
                stack.append((current_depth + 1, node.right))
        return depth

    def leave(self, p):
        """
        :param p:结点
        :return: p 结点的叶子节点总数
        """
        if self.is_empty(p):
            return 0
        elif self.is_leaf(p):
            return 1
        else:
            return self.leave(p.left) + self.leave(p.right)

    def print_bin_tree(self, t):
        """ 以 key(Left, Right) 的形式输出二叉树的各个结点 """
        if t:
            print(t.data, end='')  # 输出结点数据
            if t.left or t.right:
                print('(', end='')
                self.print_bin_tree(t.left)  # 递归输出左子树
                if t.right:  # 右子树非空
                    print(',', end='')  # 输出 ，
                self.print_bin_tree(t.right)  # 递归输出右子树
                print(')', end='')

    def get_parent(self, t, p):
        """
        :param t: 根结点
        :param p: 所指结点
        :return:指针 p 所指结点的双亲结点
        """
        if not t:
            return None
        if t == p:
            return None
        if t.left == p or t.right == p:
            return t
        s = self.get_parent(t.left, p)
        return s if s else self.get_parent(t.right, p)

    @staticmethod
    def is_symmetric(t):
        if not t:
            return True

        def formation(l, r):
            if not l and not r:
                return True
            if not l or not r:
                return False
            if l.data != r.data:
                return False
            return formation(l.left, r.right) and formation(l.right, r.left)
        return formation(t.left, t.right)

    def similar(self, t1, t2):
        """ 两个二叉树是否相似（数据可以不相等） """
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        if not self.similar(t1.left, t2.left):
            return False
        else:
            return self.similar(t1.right, t2.right)

    def pre_order(self, t):
        """ 先序遍历 """
        if t:
            print(t.data, end='')
            self.pre_order(t.left)
            self.pre_order(t.right)

    def in_order(self, t):
        """ 中序遍历 """
        if t:
            self.in_order(t.left)
            print(t.data, end='')
            self.in_order(t.right)

    def post_order(self, t):
        """ 后序遍历 """
        if t:
            self.post_order(t.left)
            self.post_order(t.right)
            print(t.data, end='')

    def stack_in_order(self, p):
        """ 中序遍历的非递归算法 """
        while p or not self.stack.is_empty():
            while p:
                self.stack.push(p)
                p = p.left
            if not self.stack.is_empty():
                p = self.stack.pop()
                print(p.data, end='')
                p = p.right

    @staticmethod
    def level_order(t):
        """ 二叉树的层次遍历 """
        queue = [t]
        while len(queue) > 0:
            node = queue.pop(0)
            print(node.data, end='')
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def create_pre_bin(self, l):
        str1 = l[self.index]
        self.index += 1
        if str1 == '#':
            return None
        root = TreeNode(str1)
        root.left = self.create_pre_bin(l)
        root.right = self.create_pre_bin(l)
        return root


if __name__ == '__main__':
    tree = Tree()
    for i in range(1, 10):
        tree.add(i)
    # for i in [1, 2, 2, 3, 4, 4, 3]:
    #     tree.add(i)
    # print(tree.leave(tree.root))
    # print(tree.height(tree.root))
    # tree.print_bin_tree(tree.root)
    # print(tree.root.left.left.right.data)
    # print(tree.get_parent(tree.root, tree.root.left.left.right).data)
    # print(tree.is_symmetric(tree.root))
    # tree.pre_order(tree.root)
    # tree.in_order(tree.root)
    # tree.post_order(tree.root)
    # tree.stack_in_order(tree.root)
    # tree.level_order(tree.root)
    pre = ['A', 'B', 'C', '#', '#', 'D', 'E', '#', 'G', '#', '#', 'F', '#', '#', '#', ';']
    tree.create_pre_bin(l=pre)
    tree.in_order(tree.create_pre_bin(pre))


