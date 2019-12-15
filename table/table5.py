class Node:
	def __init__(self, data=None):
		self.data = data
		self.next = None


class MyLinkList:
	def __init__(self):
		self.head = Node(-1)

	def create(self, list_a):
		rear = self.head
		for i in range(len(list_a)):
			rear.next = Node(list_a[i])
			rear = rear.next
		rear.next = None
		self.print_link(self.head)
		return self.head

	@staticmethod
	def print_link(head_):
		"""
		:param head_:头结点
		:return: 打印链表
		"""
		res = []
		p = head_.next
		while p:
			res.append(str(p.data))
			p = p.next
		print('->'.join(res))

	def result1(self, head_a, head_b):
		""" 第二章32 """
		p = head_b.next
		head_b.next = None
		while p:
			q = p
			p = p.next
			q.next = head_b.next
			head_b.next = q
		pa, pb = head_a.next, head_b.next
		pre = head_a
		p = pa
		while pa and pb:
			if pa.data == pb.data:
				pa, pb = pa.next, pb.next
			else:
				pre = p
				p = p.next
				pa = p
				pb = head_b.next
		if not pb:
			print('与字串匹配的起始位置在%d' % p.data)
			q = p.next
			p.next = pa
			s = q.next
			while q != pa:
				q.next = p
				p = q
				q = s
				s = s.next
			pre.next = p
			p = head_b.next
			head_b.next = None
		self.print_link(head_a)

	def result2(self, head_a, x):
		""" 把所有结点值大于等于x的连接到小于x的结点后面 """
		pr, p = head_a, head_a.next
		h = Node(-1)
		rear = h
		while p:
			if p.data >= x:
				pr.next = p.next
				rear.next = p
				rear = p
				p = p.next
			else:
				pr = p
				p = p.next
		rear.next = None
		pr.next = h.next
		self.print_link(head_a)
		self.print_link(h)

	@staticmethod
	def result3(head_a):
		pre, p, i = head_a.next, head_a.next.next, 2
		while p:
			if p.data != (i*i - pre.data):
				return False
			else:
				pre = p
				p = p.next
				i = i + 1
		return True

	def result4(self, head_a, x):
		""" 递增单链表中比x大的数字有几个，重复数字算一次 """
		p = head_a.next
		while p and p.data <= x:
			p = p.next
		if not p:
			return False
		pre = p
		p = p.next
		count = 1
		while p:
			if p.data != pre.data:
				count = count + 1
				pre = p
				p = p.next
			else:
				p = p.next
		print('在链表中比{}大的不重复的值有{}个'.format(x, count))

		""" 将比正整数x小的数按非递增（递减）顺序排列 """
		pre, p = head_a.next, head_a.next.next
		while p and p.data < x:
			pre.next = p.next
			p.next = head.next
			head.next = p
			p = pre.next
		self.print_link(head_a)

	def result5(self, head_a):
		stack = []
		p = head_a.next
		while p:
			stack.append(p.data)
			p = p.next
		print(stack)
		p = head_a.next
		while p:
			x = stack.pop(-1)
			if p.data != x:
				return False
			p = p.next
		return True


if __name__ == '__main__':
	list_a = [1, 3, 4, 6, 7, 9]
	list_b = [7, 6, 4]
	link = MyLinkList()
	head = link.create(list_a)

	# link2 = MyLinkList()
	# head2 = link2.create(list_b)

	# link.result1(head, head2)
	# link.result2(head, 5)
	# link.result4(head, 6)
	print(link.result5(head))
