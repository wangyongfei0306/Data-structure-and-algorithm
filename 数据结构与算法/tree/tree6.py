class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.right = right
        self.left = left


class Start:
    def __init__(self, string):
        self.string = string
        self.root = None
        self.index = 0
        self.result = []
        self.max_node = -999
        self.count = 1

    def create_tree(self):
        self.root = self.construct_tree()
        self.mid_order(self.root)

    def construct_tree(self):
        """ 根据 self.string（它的顺序是先序遍历的结果） 构建一个二叉树 """
        str1 = self.string[self.index]
        self.index += 1
        if str1 == '#':
            return None
        root = Node(str1)
        root.left = self.construct_tree()
        root.right = self.construct_tree()
        return root

    def mid_order(self, root):
        """ 根据创建的二叉树打印中序遍历的结果 """
        if not root:
            return
        self.mid_order(root.left)
        self.result.append(root.data)
        self.mid_order(root.right)

    def build_tree(self, pre_order, in_order):
        """
        :param pre_order:先序遍历的结果
        :param in_order: 中序遍历的结果
        :return: 构建的树的根结点
        """
        if len(in_order) == 0:
            return None
        root = Node(pre_order[0])
        mid = in_order.index(pre_order[0])
        root.left = self.build_tree(pre_order[1:mid+1], in_order[:mid])
        root.right = self.build_tree(pre_order[mid+1:], in_order[mid+1:])
        return root

    @staticmethod
    def build_tree2(pre_ord, in_ord):
        """ build_tree方法的另一种实现 """
        pre_index = 0
        idx_map = {val: idx for idx, val in enumerate(in_ord)}

        def helper(in_left=0, in_right=len(in_ord)):
            nonlocal pre_index
            if in_left == in_right:
                return None
            root_val = pre_ord[pre_index]  # 创建结点数据
            root = Node(root_val)
            index = idx_map[root_val]
            pre_index = pre_index + 1
            root.left = helper(in_left, index)
            root.right = helper(index+1, in_right)
            return root
        return helper()

    def post_print(self, root):
        if not root:
            return None
        self.post_print(root.left)
        self.post_print(root.right)
        print(root.data, end=' ')

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

    def pre_print(self, root):
        if not root:
            return None
        print(root.data, end=' ')
        self.pre_print(root.left)
        self.pre_print(root.right)

    def print_node_level(self, root, i):
        if not root:
            return None
        print('结点的值为{}，所在层次为{}'.format(root.data, i))
        self.print_node_level(root.left, i + 1)
        self.print_node_level(root.right, i + 1)

    def degrees_1(self, root):
        """ 统计二叉树中度为1的结点的个数 """
        if not root:
            return 0
        if root.left and not root.right:
            return 1 + self.degrees_1(root.left)
        elif not root.left and root.right:
            return 1 + self.degrees_1(root.right)
        else:
            return self.degrees_1(root.left) + self.degrees_1(root.right)

    def degrees_2(self, root):
        """ 统计二叉树中度为2的结点的个数 """
        if not root:
            return 0
        if root.left and root.right:
            return 1 + self.degrees_2(root.left) + self.degrees_2(root.right)
        else:
            return self.degrees_2(root.left) + self.degrees_2(root.right)

    def degrees_0(self, root):
        """ 统计二叉树中度为0的结点的个数 """
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        return self.degrees_0(root.left) + self.degrees_0(root.right)

    def height(self, root):
        """ 树的高度 """
        if not root:
            return 0
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        return 1 + max(left_height, right_height)

    def level_node(self, t, p, d):
        """
        :param t: 根结点
        :param p: 指定结点的数据
        :param d: 初始根结点的深度为1
        :return: 返回指定结点的深度
        """
        if not t:
            return 0
        if t.data == p:
            return d
        depth = self.level_node(t.left, p, d + 1)
        if depth:
            return depth
        else:
            return self.level_node(t.right, p, d+1)

    def max_val(self, root):
        """ 最大元素值 """
        if not root:
            return None
        else:
            if root.data > self.max_node:
                self.max_node = root.data
            self.max_val(root.left)
            self.max_val(root.right)
        return self.max_node

    def pre_search_k(self, t, k):
        """ 利用先序遍历求先序遍历的第k个结点 """
        if t:
            if self.count == k:
                return t
            self.count += 1
            p = self.pre_search_k(t.left, k)
            if p:
                return p
            else:
                return self.pre_search_k(t.right, k)
        else:
            return None

    def del_tree(self, r):
        """ 删除二叉树中的全部结点 """
        while r:
            self.del_tree(r.left)
            self.del_tree(r.right)
            r = None
        return r

    def del_sub(self, t, p):
        """ 删除以p为根结点的子树 """
        if t:
            if t == p:
                self.del_tree(t)
            else:
                self.del_sub(t.left, p)
                self.del_sub(t.right, p)

    def split_tree(self, t, x):
        """ 将以x为根的子树拆分出来，使原二叉树分成两棵树 """
        if t.data == x or not t:
            return None
        if t.left and t.left.data == x:
            sub = t.left
            t.left = None
            return sub
        if t.right and t.right.data == x:
            sub = t.right
            t.right = None
            return sub
        sub = self.split_tree(t.left, x)
        return sub if sub else self.split_tree(t.right, x)


if __name__ == '__main__':
    # pre = ['A', 'B', 'C', '#', '#', '#', 'D', 'E', '#', '#', 'F', '#', '#']
    # begin = Start(pre)
    # begin.create_tree()
    # answer = ' '.join(begin.result)
    # answer += ' '
    # print('中序遍历的结果：', answer)

    # pre_order = [3, 9, 20, 15, 7]
    # in_order = [9, 3, 15, 20, 7]
    # begin = Start('')
    # begin.post_print(begin.build_tree2(pre_order, in_order))

    begin = Start('')
    post_ord = [15, 20, 7, 6, 9, 3]
    in_ord = [15, 7, 20, 3, 6, 9]
    t = begin.create_tree_pre_in(post_ord, in_ord)
    # begin.pre_print(t)

    # begin.print_node_level(t, 1)

    # print(begin.degrees_2(t))

    # print(begin.height(t))

    # print(begin.level_node(t, 9, 1))

    # print(begin.max_val(t))

    # print(begin.pre_search_k(t, 5 ).data)

    # print(begin.del_tree(t))

    # print(begin.split_tree(t, 9))
    begin.pre_print(begin.split_tree(t, 9))
    begin.pre_print(t)
