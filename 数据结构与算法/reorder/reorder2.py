def shaker_sort(ary):
    """
    双向起泡排序
    :param ary: 待排序组
    :return: 有序数组
    """
    low, high = 0, len(ary) - 1
    exchange = True
    while low < high and exchange:
        exchange = False
        i = low
        while i < high:
            if ary[i] > ary[i+1]:
                ary[i], ary[i+1] = ary[i+1], ary[i]
                exchange = True
            i += 1
        high -= 1
        i = high
        while i > low:
            if ary[i] < ary[i-1]:
                ary[i], ary[i-1] = ary[i-1], ary[i]
                exchange = True
            i -= 1
        low += 1
    return ary


def shaker_sort_1(ary):
    low, high = 0, len(ary) - 1
    while low < high:
        j = low
        i = low
        while i < high:
            if ary[i] > ary[i+1]:
                ary[i], ary[i+1] = ary[i+1], ary[i]
                j = i  # 正序时最后交换位置的编号
            i += 1
        high = j  # 更新正序时的最高位
        i = high
        while i > low:
            if ary[i] < ary[i-1]:
                ary[i], ary[i-1] = ary[i-1], ary[i]
                j = i  # 逆序时最后交换位置的编号
            i -= 1
        low = j  # 更新逆序时的最低位
    return ary


def re_arrange(ary):
    """ 所有的负数在正数的前面 """
    i, j = 0, len(ary)-1
    while i < j:
        while i < j and ary[j] >= 0:
            j -= 1
        while i < j and ary[i] < 0:
            i += 1
        if i < j:
            ary[i], ary[j] = ary[j], ary[i]
            i += 1
            j -= 1
    return ary


def partition_1(ary, low, high):
    i, j = low, high
    pivot = ary[low]
    while i != j:
        while i < j and ary[j] >= pivot:
            j -= 1
        if i < j:
            ary[i] = ary[j]
            i += 1
        while i < j and ary[i] <= pivot:
            i += 1
        if i < j:
            ary[j] = ary[i]
            j -= 1
    ary[i] = pivot
    return i


def find_kth(ary, k):
    n = len(ary)
    if k < 1 or k > n:
        return -1
    left, right = 0, n-1
    while 1:
        m = partition_1(ary, left, right)
        if m+1 > k:
            right = m - 1
        elif m+1 < k:
            left = m + 1
        else:
            return ary[m]


def find_max_k(ary, k, low, high):
    i, j = low, high
    tmp = ary[low]
    while i < j:
        while i < j and ary[j] >= tmp:
            j -= 1
        if i < j:
            ary[i] = ary[j]
            i += 1
        while i < j and ary[i] < tmp:
            i += 1
        if i < j:
            ary[j] = ary[i]
            j -= 1
    ary[i] = tmp
    if high-i == k:
        return i + 1
    elif high - i > k:
        return find_max_k(ary, k, i+1, high)
    else:
        return find_max_k(ary, k-high+i, low, i)


def re_arrange_sort(ary):
    """ 奇数在奇下标位，偶数在偶下标位。ary一半奇数一半偶数 """
    i, j, n = 0, 1, len(ary)
    while i < n and j < n:
        while i < n and ary[i] % 2 == 0:
            i += 2
        while j < n and ary[j] % 2 == 1:
            j += 2
        if i < n and j < n:
            ary[i], ary[j] = ary[j], ary[i]
            i += 2
            j += 2
    return ary


def select_sort(ary, left, right):
    """ 一个简单的选择排序 """
    if left < right:
        k = left
        i = left + 1
        while i <= right:
            if ary[k] > ary[i]:
                k = i
            i += 1
        if left != k:
            ary[left], ary[k] = ary[k], ary[left]
        select_sort(ary, left+1, right)
    return ary


def double_select_sort(ary, left, right):
    if left >= right:
        return
    i = left
    Min, Max = left, right
    while i <= right:
        if ary[i] < ary[Min]:
            Min = i
        if ary[i] > ary[Max]:
            Max = i
        i += 1
    if Max == left:
        ary[Max], ary[Min] = ary[Min], ary[Max]
        Max = Min
    elif Min != left:
        ary[Min], ary[left] = ary[left], ary[Min]
    if Max != right:
        ary[Max], ary[right] = ary[right], ary[Max]
    double_select_sort(ary, left+1, right-1)
    return ary


if __name__ == '__main__':
    # print(shaker_sort([5, 1, 4, 2, 3]))
    # print(shaker_sort_1([5, 1, 4, 2, 3]))
    # print(re_arrange([1, -2, 3, -5, 0, 4]))
    # print(partition_1([5, 2, 6, 4, 7, 10], 0, 5))
    # print(find_kth([5, 2, 6, 4, 7, 10], 4))
    # print(find_max_k([5, 2, 6, 4, 7, 10], 2, 0, 5))
    # print(re_arrange_sort([5, 2, 6, 4, 7, 1]))
    # print(select_sort([5, 2, 6, 4, 7, 10], 0, 5))
    print(double_select_sort([5, 2, 6, 4, 7, 10], 0, 5))
