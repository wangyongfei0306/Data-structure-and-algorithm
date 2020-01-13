class Tree:
    class Position:
        def element(self):
            raise NotImplementedError('must be implemented by subclass')

        def __eq__(self, other):
            raise NotImplementedError('must be implemented by subclass')

        def __ne__(self, other):
            return not (self == other)

    def root(self):
        raise NotImplementedError('must be implemented by subclass')

    def parent(self, p):
        raise NotImplementedError('must be implement by subclass')

    def num_children(self, p):
        raise NotImplementedError('must be implement by subclass')

    def children(self, p):
        raise NotImplementedError('must be implement by subclass')

    def __len__(self):
        raise NotImplementedError('must be implement by subclass')

    def is_root(self, p):
        return self.root() == p

    def is_leaf(self, p):
        return self.num_children(p) == 0

    def is_empty(self):
        return len(self) == 0

    def depth(self, p):
        """
        :param p:输入结点的信息
        :return: 返回结点的深度
        """
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))


