def insert_sort(ary, kcn, rmn):
    i, j = 1, 0
    n = len(ary)
    while i <= n - 1:
        kcn += 1
        if ary[i] < ary[i - 1]:
            tmp = ary[i]
            ary[i] = ary[i - 1]
            rmn += 2
            j = i - 2
            while j >= 0:
                kcn += 1
                if tmp >= ary[j]:
                    break
                else:
                    ary[j + 1] = ary[j]
                    rmn += 1
                j -= 1
            ary[j + 1] = tmp
            rmn += 1
        i += 1
    return kcn, rmn, ary


def insert_last2(ary):
    """ 前n-2个元素已经递增排好序，把所有的尽快排好 """
    n = len(ary)
    large = max(ary[n - 1], ary[n - 2])  # 取出最后两个元素中最大的值
    small = min(ary[n - 1], ary[n - 2])  # 取出最后两个元素中最小的值
    j = n - 3                            # 从n-3开始反向寻找
    while j >= 0 and ary[j] > large:     # 第j号大于最大的值时往左边寻找插入位置
        ary[j + 2] = ary[j]              # 最大的后移两个元素的位置
        j -= 1                           # j减一继续判断
    ary[j + 2] = large                   # 插入最大的值
    while j >= 0 and ary[j] > small:     # 第j号大于最小的值时往左边寻找插入位置
        ary[j + 1] = ary[j]              # 此时的j元素后移一个位置
        j -= 1                           # j减一继续判断
    ary[j + 1] = small                   # 插入最小值
    return ary                           # 返回排好序的数组


def double_insert_sort(target, assist):
    """
    :param target: 目标待排序列
    :param assist: 辅助序列
    :return: 实现一个二路插入排序，返回排好的target
    """
    n = len(target)
    first, final = n - 1, -1                    # 指针first指向assist[n-1]位置，final指向-1
    assist[n-1] = target[0]                     # 把target序列的第一个元素放在assist的最后以为作为基准
    i = 1                                       # assist[n-1]视为排好序的数组的中间位置
    while i < n:
        if target[i] < assist[n-1]:             # 小于基准插入左边
            j = first
            while j <= n-2:                     # 判断插入位置
                if target[i] > assist[j]:
                    assist[j-1] = assist[j]
                else:
                    break
                j += 1
            assist[j-1] = target[i]
            first -= 1
        else:                                   # 大于基准插入右边
            j = final
            while j >= 0:
                if target[i] < assist[j]:
                    assist[j+1] = assist[j]
                else:
                    break
                j -= 1
            assist[j+1] = target[i]
            final += 1
        i += 1

    i, j = 0, first                             # 传送回target序列排序好后的结果
    while j < n:
        target[i] = assist[j]
        i += 1
        j += 1
    j = 0
    while j <= final:
        target[i] = assist[j]
        i += 1
        j += 1
    return target, assist


def link_insert_sort(link_head):
    q = link_head.next
    link_head.next = None
    while q:
        pre = link_head
        p = link_head.next
        while p and p.data <= q.data:
            pre = p
            p = p.next
        pre.next = q
        q = q.next
        pre.next.next = p
    return link_head


def binary_insert_sort(ary):
    """ 在折半插入排序中让插入位置和后移元素在同一个循环中进行 """
    i, n = 1, len(ary)
    while i <= n-1:
        if ary[i] < ary[i-1]:
            temp = ary[i]
            low, high = 0, i-1
            while low <= high:
                mid = (low + high) // 2
                if temp < ary[mid]:
                    j = high
                    while j >= mid:
                        ary[j+1] = ary[j]
                        j -= 1
                    high = mid - 1
                else:
                    low = mid + 1
            ary[low] = temp
        i += 1
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
    return ary


def unknown(ary):
    high = len(ary) - 1
    while high > 0:
        i, j = 0, 0
        while i < high:
            if ary[i] > ary[i+1]:
                ary[i], ary[i+1] = ary[i+1], ary[i]
                j = i
            i += 1
        high = j
    return ary


if __name__ == '__main__':
    # l1 = insert_sort([1, 3, 2] , 0, 0)
    # print(l1)

    # print(insert_last2([1, 2, 4, 0, 3]))
    # print(double_insert_sort([49, 38, 65, 97, 76, 13, 27, 54], [None]*8))

    # link_head = MyLinkList().create([5, 6, 1, 2, 4, 3])
    # new_head = link_insert_sort(link_head)
    # MyLinkList().print_link(new_head)

    # print(binary_insert_sort([1, 2, 8, 6, 7, 5, 9]))

    # print(partition_1([5, 3, 4, 1, 2], 0, 4))

    print(unknown([5, 3, 4, 1, 2]))
