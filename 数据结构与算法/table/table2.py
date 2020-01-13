class Node:
	def __init__(self, data=None):
		self.data = data
		self.next = None
		
		
class MyLinkList:
	def __init__(self):
		self.head = Node()
		self.size = 0
		self.rear = 0

	""" 尾插法 """
	def create(self, A):
		self.head = Node(-1)
		self.rear = self.head
		
		for i in range(len(A)):
			self.rear.next = Node(A[i])
			self.rear = self.rear.next
			self.size += 1
		self.rear.next = None
		return self.head

	""" 头插法 """
	def create2(self, A):
		self.head = Node(-1)
		for i in range(len(A)):
			node = Node(A[i])
			node.next = self.head.next
			self.head.next = node
			self.size += 1
		return self.head

	""" 寻找第 i 个结点 """
	@staticmethod
	def get_node(node, i):
		"""
		:param node: 链表的头结点
		:param i: 链表中的第几个结点
		:return: 返回第i个结点的地址
		"""
		count, p = 0, node
		if i < 0:
			return None
		while (p is not None) and count < i:
			p = p.next
			count += 1
		return p

	""" 倒数第k个结点 """
	@staticmethod
	def get_node2(node, k):
		q = p = node.next
		count, n = 1, 1
		while p.next:
			p = p.next
			n += 1
			if count < k:
				count += 1
			else:
				q = q.next
		if k <= 0 or k > n:
			return 0
		else:
			print('倒数第', k, '个结点值是：', q.data)
			return 1

	def Max_Node(self, Head):
		if Head.next is None:
			return None
		p = Head.next  # 首元结点
		max_node = -1
		while p:
			max_node = max(max_node, p.data)
			p = p.next
		return max_node

	def count_link(self, Head):
		"""
		:param Head: 头结点
		:return: 返回链表结点数
		"""
		p = Head.next
		count = 0
		while p is not None:
			count += 1
			p = p.next
		return count

	""" 指定值出现的次数 """
	def count_node(self, Head, x):
		p = Head.next
		count = 0
		if not p:
			return -1
		while p:
			if p.data == x:
				count += 1
			p = p.next
		return count


if __name__ == '__main__':
	A = [1, 3, 5, 7, 9]
	link = MyLinkList()
	# print(link.create(A))
	# print('--------')
	# print(link.size)
	# print('--------')
	# print('头结点：', link.head.data, link.head.next)
	# print('首元结点：', link.head.next.data, link.head.next.next)
	# print('第二结点：', link.head.next.next.data, link.head.next.next.next)
	# print('第三结点：', link.head.next.next.next.data)
	# print('第四结点：', link.head.next.next.next.next.data)
	# print('第五结点：', link.head.next.next.next.next.next.data)

	# print(link.create2(A), link.size)
	# print(link.head.data, link.head.next.data, link.head.next.next.data)

	# head = link.create(A)
	# print(link.get_node(head, 3).data)

	# head = link.create(A)
	# link.get_node2(head, 2)

	# head = link.create(A)
	# print(link.Max_Node(head))

	# head = link.create(A)
	# print(link.count_link(head))

	# head = link.create(A)
	# print(link.count_node(head, 5))
