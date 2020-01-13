class Node:
	def __init__(self, data=None):
		self.data = data
		self.next = None


class MyLinkedList:
	def __init__(self):
		self.head = None
		self.p = None

	def create(self, list_a):
		self.head = None
		self.p = None
		for i in range(len(list_a)):
			node = Node(list_a[i])
			if not self.head:
				self.head = self.p = node
			else:
				self.p.next = node
				self.p = self.p.next
		self.print_result(self.head)
		return self.head

	def print_result(self, HEAD):
		res = []
		p = HEAD
		while p:
			res.append(str(p.data))
			p = p.next
		print('->'.join(res))

	def result(self, Head, Head2):
		""" 两个无头结点递增排列的有序单链表，合并成一个非递增次序排列的单链表 """
		pa, pb = Head, Head2
		head, q = None, None
		while pa and pb:
			if pa.data < pb.data:
				q = pa
				pa = pa.next
			else:
				q = pb
				pb = pb.next
			q.next = head
			head = q
		if not pa:
			pa = pb
		while pa:
			q = pa
			pa = pa.next
			q.next = head
			head = q
		self.print_result(head)
		return head

	def result2(self, Head):
		""" 反转一个无头结点的单链表(一次遍历) """
		p = Head.next  # 第二个结点
		Head.next = None
		while p:
			q = p
			p = p.next
			q.next = Head
			Head = q
		self.print_result(Head)


if __name__ == '__main__':
	list_a = [1, 3, 5, 6, 8, 9]
	list_b = [0, 2, 4, 7]
	""" 没有头结点的链表 """
	link = MyLinkedList()
	Head = link.create(list_a)
	# Head2 = link.create(list_b)
	# print(link.result(Head, Head2))
	link.result2(Head)

