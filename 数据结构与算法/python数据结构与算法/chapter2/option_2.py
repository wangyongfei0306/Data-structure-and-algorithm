class Vector:

    def __init__(self, d):
        self._cords = [0] * d

    def __len__(self):
        return len(self._cords)

    def __getitem__(self, item):
        return self._cords[item]

    def __setitem__(self, key, value):
        self._cords[key] = value

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __eq__(self, other):
        return self._cords == other._cords

    def __str__(self):
        return '<' + str(self._cords)[1:-1] + '>'


class Sequencelterator:

    def __init__(self, sequence):
        self._seq = sequence
        self._k = -1

    def __next__(self):
        self._k += 1
        if self._k < len(self._seq):
            return self._seq[self._k]
        else:
            raise StopIteration()

    def __iter__(self):
        pass
        return self


if __name__ == '__main__':
    # v = Vector(5)
    # v[1] = 23
    # v[-1] = 45
    # for i in v:
    #     print(i, end=' ')
    # print('\n')
    # print(v[4])
    # u = v + v
    # print(u)
    #
    # total = 0
    # for entry in v:
    #     total += entry
    #     print(total)

    seq = Sequencelterator([1, 2, 3, 4])
    for i in seq:
        print(i)