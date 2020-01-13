"""
get(index)：获取链表中第 index 个节点的值。如果索引无效，则返回-1。
addAtHead(val)：在链表的第一个元素之前添加一个值为 val 的节点。插入后，新节点将成为链表的第一个节点。
addAtTail(val)：将值为 val 的节点追加到链表的最后一个元素。
addAtIndex(index,val)：在链表中的第 index 个节点之前添加值为 val  的节点。
如果 index 等于链表的长度，则该节点将附加到链表的末尾。如果 index 大于链表长度，则不会插入节点。如果index小于0，则在头部插入节点。
deleteAtIndex(index)：如果索引 index 有效，则删除链表中的第 index 个节点。
"""


class ListNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = ListNode()
        self.length = 0

    def get(self, index: int) -> int:
        j = 0
        if index > self.length-1 or index < 0:
            return -1
        if not self.head.next:
            return -1
        p = self.head
        while j < index and p.next:
            p = p.next
            j += 1
        return p.val

    def addAtHead(self, val: int) -> None:
        new = ListNode(val)
        new.next = self.head.next
        self.head.next = new

    def addAtTail(self, val: int) -> None:
        new = ListNode(val)
        if self.head.next:
            p = self.head
            while p.next:
                p = p.next
            p.next = new
        else:
            self.head.next = new
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        pass

    def deleteAtIndex(self, index: int) -> None:
        pass

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)


# class ListNode2:
#     def __init__(self, value=None):
#         self.value = value
#         self.next = None
#
#
# class MyLinkedList2:
#     def __init__(self):
#         self.head = ListNode2()
#         self.length = 0
#
#     def add(self, value):
#         new = ListNode2(value)
#         if self.head:
#             p = self.head
#             while p.next:
#                 p = p.next
#             p.next = new
#         else:
#             self.head.next = new
#         self.length += 1
#
#
# list2 = MyLinkedList2()
# print(list2.length)
#
# list2.add(1)
# print(list2.head.next.value, list2.length)
#
# first_node = list2.head.next
# list2.add(2)
# print(first_node.next.value, list2.length)
#
# list2.add(3)
# print(first_node.next.next.value, list2.length)
