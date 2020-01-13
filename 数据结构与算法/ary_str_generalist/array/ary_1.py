from datetime import time


def main(max_size):
    ary = [None] * max_size
    i = 0
    while i <= max_size-1:
        ary[i] = i + 1
        i += 1
    print(ary)
    ary[max_size-1] = 0
    print(ary)
    i = 0
    while i < max_size:
        print(ary[i], end=' ')
        i += 1


def is_ascend(ary, i, n):
    """ 用递归的方法判断序列是否升序 """
    if i == n-1 or i == n:
        return True
    if not is_ascend(ary, i+1, n):
        return False
    if ary[i] < ary[i+1]:
        return True
    else:
        return False


def reversed(ary):
    print(ary)
    i, j = 0, len(ary)-1
    while i <= j:
        ary[i], ary[j] = ary[j], ary[i]
        i += 1
        j -= 1
    print(ary)


def max_length(ary, n, x):
    if x == 0 or n == 0:
        return 0
    left, right, len_, sum_ = 0, 0, 0, ary[0]
    while right < n:
        if sum_ == x:
            if len_ < right+1-left:
                len_ = right+1-left
            sum_ -= ary[left]
            left += 1
        elif sum_ < x:
            right += 1
            if right == n:
                break
            sum_ += ary[right]
        else:
            sum_ -= ary[left]
            left += 1
    return len_


def first_odd_last_even(ary, n):
    i, j = 0, n-1
    while i < j:
        while ary[i] % 2 == 1:
            i += 1
        while ary[j] % 2 == 0:
            j -= 1
        if i < j:
            ary[i], ary[j] = ary[j], ary[i]
            i += 1
            j -= 1
    return ary


def pattern(ary, ary2):
    m, n = len(ary), len(ary2)
    j = 0
    k = 0
    while k < m and j < n:
        i = k
        while i < m and j < n:
            if ary[i] == ary2[j]:
                i += 1
                j += 1
            else:
                j = 0
                break
        k += 1
    if j == n:
        return True
    else:
        return False


def f(n):
    if n == 1:
        return 1
    return n * f(n-1)


if __name__ == '__main__':
    # main(6)
    # print(is_ascend([1, 2, 5, 4], 0, 4))
    # reversed([1, 3, 5, 6, 8])
    # print(max_length([1, 2, 1, 1, 1], 5, 3))
    # print(first_odd_last_even([1, 2, 3, 4, 5], 5))
    # print(pattern([1, 3, 0, 3, 4, 5], [3, 4]))
    # print(f(180))


    pass
print('hello'.index('l'))