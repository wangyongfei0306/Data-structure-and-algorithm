class Search:
    def __init__(self):
        self.l = [2, 4, 6, 8, 10]

    def search1(self, x):
        """ 折半查找 """
        n = len(self.l)
        left, right = 0, n-1
        while left <= right:
            mid = (left + right) // 2
            if self.l[mid] == x:
                return mid
            elif self.l[mid] < x:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    def seq_search(self, x, loc):
        """
        :param x: 目标值
        :param loc: 指明开始查找的位置
        :return: 目标值所处的位置
        """
        if loc >= len(self.l):
            return -1
        if self.l[loc] == x:
            return loc
        else:
            return self.seq_search(x, loc+1)


if __name__ == '__main__':
    begin = Search()
    # print(begin.search1(8))

    print(begin.seq_search(6, 0))
