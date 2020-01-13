from 数据结构与算法.table.table4 import MyLinkedList, Node


def link_select_sort(head):
    """ 在单链表上进行简单选择排序 """
    h = head.next
    head.next = None
    while h:
        """ s,r 是最大结点和它的前驱，p,q 是任意节点和它的前驱 """
        p = s= h
        q = r = None
        while p:
            if p.data > s.data:
                s = p
                r = q
            q = p
            p = p.next
        if s == h:
            h = h.next
        else:
            r.next = s.next
        s.next = head.next
        head.next = s
    return head


def merge_half(ary, left, right):
    """ 数组ary里面有两个有序的子数组，合并成一个完整的有序数组 """
    print('待排序数组：', ary)
    mid = (left + right) // 2
    m = mid + 1 - left
    assist = [None] * m
    i = left
    while i <= mid:
        assist[i] = ary[i]
        i += 1
    print('辅助数组长度大小为{}：'.format(m), assist)
    i, j, k = 0, mid+1, left
    while i < m and j <= right:
        if assist[i] <= ary[j]:
            ary[k] = assist[i]
            k += 1
            i += 1
        else:
            ary[k] = ary[j]
            k += 1
            j += 1
    while i < m:
        ary[k] = assist[i]
        k += 1
        i += 1
    print('排好序的数组：', ary)


def merge_binary(ary, left, right):
    mid = (left + right) // 2
    d = left
    i = mid + 1
    while i <= right:
        if ary[i] < ary[i-1]:
            j, k = d, i-1
            tmp = ary[i]
            while j <= k:
                s = (j + k) // 2
                if ary[s] > tmp:
                    k = s - 1
                else:
                    j = s + 1
            s = i - 1
            while s >= j:
                ary[s+1] = ary[s]
                s -= 1
            ary[j] = tmp
        i += 1
    print(ary)


def Link_merge(head1, head2):
    if not head1:
        result = head2
    elif not head2:
        result = head1
    else:
        head = Node(-1)
        p1, p2, r = head1, head2, head
        while p1 and p2:
            if p1.data <= p2.data:
                r.next = p1
                r = p1
                p1 = p1.next
            else:
                r.next = p2
                r = p2
                p2 = p2.next
        r.next = p1 if p1 else p2
        result = head.next
    return result


if __name__ == '__main__':
    # link = MyLinkList()
    # head = link.create([5, 4, 6, 3, 9, 1])
    # new_head = link_select_sort(head)
    # link.print_link(new_head)

    # merge_half([2, 5, 7, 9, 1, 3, 4, 6], 0, 7)
    # merge_binary([2, 5, 7, 9, 1, 3, 4, 6], 0, 7)

    # 没有头结点的链表
    link1 = MyLinkedList()
    head1 = link1.create([1, 3, 5, 7, 9])
    link2 = MyLinkedList()
    head2 = link2.create([2, 4, 6, 8, 10])
    new_head = Link_merge(head1, head2)
    link1.print_result(new_head)

    pass

