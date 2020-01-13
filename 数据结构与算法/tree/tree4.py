class Node:
    def __init__(self, item):
        self.elem = item
        self.left_child = None
        self.right_child = None


class Tree:
    def __init__(self):
        self.root = None

    def add(self, item):
        node = Node(item)

        if self.root is None:
            self.root = node
            return

        queue = [self.root]

        while queue:
            cur_node = queue.pop(0)  # 弹出列表的第一个元素
            if cur_node.left_child is None:  # 结点左孩子为空时
                cur_node.left_child = node  # 把这个结点元素添加到左边
                return
            else:
                queue.append(cur_node.left_child)  # 不为空时，把这个结点添加到列表

            if cur_node.right_child is None:
                cur_node.right_child = node
                return
            else:
                queue.append(cur_node.right_child)

    def breadth_travel(self):
        """ 广度遍历（横向遍历） """
        if self.root is None:
            return

        queue = [self.root]

        while queue:
            cur_node = queue.pop(0)
            print(cur_node.elem, end='')
            if cur_node.left_child is not None:
                queue.append(cur_node.left_child)
            if cur_node.right_child is not None:
                queue.append(cur_node.right_child)

    def pre_order(self, node):
        """ 先序遍历 """
        if node is None:
            return
        print(node.elem, end='')
        self.pre_order(node.left_child)
        self.pre_order(node.right_child)

    def in_order(self, node):
        """ 中序遍历 """
        if node is None:
            return
        self.in_order(node.left_child)
        print(node.elem, end='')
        self.in_order(node.right_child)

    def post_order(self, node):
        """ 后序遍历 """
        if node is None:
            return
        self.post_order(node.left_child)
        self.post_order(node.right_child)
        print(node.elem, end='')

    def pre_order_stack(self, node):
        """ 非递归前序遍历 """
        # if node is None:
        #     return
        # s = Stack()
        #
        # while node:
        #     print(node.elem, end='')
        #     s.push(node)
        #     node = node.left_child
        # while not s.empty():
        #     s.pop()
        pass

    def in_order_stack(self, node):
        """ 非递归中序遍历 """
        pass

    def post_order_stack(self, node):
        """ 非递归后序遍历 """
        pass

    def count(self, node):
        n1 = n2 = 0
        if node is None:
            return 0
        else:
            n1 = self.count(node.left_child)
            n2 = self.count(node.right_child)
        return n1 + n2 + 1


if __name__ == '__main__':
    tree = Tree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    print('广度遍历:', tree.breadth_travel())
    print('先序遍历:', tree.pre_order(tree.root))
    print('中序遍历:', tree.in_order(tree.root))
    print('后序遍历:', tree.post_order(tree.root))
    print(tree.count(tree.root))
    print(tree.root.left_child.elem)