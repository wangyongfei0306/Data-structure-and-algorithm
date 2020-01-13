class Node:
	def __init__(self, data=None):
		self.data = data
		self.next = None


class MyLinkList:
	def __init__(self):
		self.head = Node(-1)
		self.rear = 0
		self.size = 0

	def create(self, list_a):
		self.rear = self.head

		for i in range(len(list_a)):
			node = Node(list_a[i])
			self.rear.next = node
			self.rear = self.rear.next
			self.size += 1
		self.rear.next = None
		self.print_result(self.head)  # 打印链表
		return self.head

	def print_result(self, HEAD):
		p = HEAD.next
		res = []
		while p:
			res.append(str(p.data))
			p = p.next
		print('->'.join(res))

	def result1(self, Head):
		""" 删除链表中最小的结点 """
		if not Head.next:
			return False
		pre = p = Head
		pmin = p.next
		while p.next:
			if p.next.data < pmin.data:
				pre = p
				pmin = p.next
			p = p.next
		pre.next = pmin.next
		print(pmin.data)
		self.print_result(self.head)
		return True

	def result2(self, Head):
		""" 找到最小的结点并插入到头结点之后 """
		if not Head.next:
			return False
		pre = p = Head
		pmin = p.next
		while p.next:
			if p.next.data < pmin.data:
				pre = p
				pmin = p.next
			p = p.next
		pre.next = pmin.next  # 先断开最小的结点，保存在了pmin中
		pmin.next = Head.next
		Head.next = pmin
		self.print_result(Head)

	def result3(self, Head):
		""" 判断带头结点的单链表是否非递减有序 """
		p = Head.next  # 首元结点
		while p.next:
			if p.data <= p.next.data:
				p = p.next
			else:
				print('不是非递减有序.')
				return False
		print('是非递减有序.')
		return True

	def result4(self, Head):
		""" 在有序链表中删除相同值的多余结点 """
		p = Head.next
		while p and p.next:
			if p.data == p.next.data:
				p.next = p.next.next
			else:
				p = p.next
		self.print_result(Head)

	def result5(self, Head):
		""" 在无序链表中删除相同值的多余结点 """
		pre = Head.next
		p = pre.next
		while p:
			r = Head.next
			while r != p:
				if r.data == p.data:
					break
				r = r.next
			if r != p:
				pre.next = p.next
				p = pre.next
			else:
				pre = p
				p = p.next
		self.print_result(Head)

	def result6(self, Head):
		""" 求链表中所有整数的平均值 """
		p = Head.next
		sun, n = 0, 0
		while p:
			sun = sun + p.data
			n = n + 1
			p = p.next
		return sun/n

	def result7(self, A, B):
		""" 判断B链表是A链表的子序列 """
		pa, pb = A.next, B.next
		Next = A.next
		while pa and pb:
			if pa.data == pb.data:
				pa = pa.next
				pb = pb.next
			else:
				Next = Next.next
				pa = Next
				pb = B.next
		if pa is None:
			return False
		else:
			return True

	def result8(self, Head, Min, Max):
		""" 删除表(无序)中所有大于Min，小于Max的元素 """
		pre = Head
		p = pre.next
		while p:
			if Min < p.data < Max:
				pre.next = p.next
				p = p.next
			else:
				pre = p
				p = p.next
		self.print_result(Head)

	def result9(self, Head, Min, Max):
		""" 同result8，表有序 """
		pre = Head.next
		p = pre.next
		while p and p.data < Min:
			pre = p
			p = p.next
		while p and p.data < Max:
			pre.next = p.next
			p = p.next
		self.print_result(Head)

	def result10(self, Head):
		""" 将链表分成奇偶链表 """
		head1 = Node(-1)
		p1 = head1
		head2 = Node(-1)
		p2 = head2
		p = Head.next
		while p:
			if p.data % 2 == 1:
				p1.next = Node(p.data)
				p1 = p1.next
			else:
				p2.next = Node(p.data)
				p2 = p2.next
			p = p.next
		self.print_result(Head)
		self.print_result(head1)
		self.print_result(head2)

	def result11(self, Head):
		""" 把有序链表中的数据值为奇数的放到偶数的前面 """
		pre = Head
		p = Head.next
		h = Node(-1)
		rear = h
		while p:
			if p.data % 2 == 0:
				pre.next = p.next
				rear.next = p
				rear = p
				p = p.next
			else:
				pre = p
				p = p.next
		rear.next = None
		pre.next = h.next
		self.print_result(Head)

	def result12(self, A, B):
		""" 两个单链表交叉合并 """
		pa, pb = A.next, B.next
		C = Node(-1)
		pc = C
		while pa and pb:
			pc.next = pa
			pc = pc.next
			pa = pa.next
			pc.next = pb
			pc = pc.next
			pb = pb.next
		if pa:
			pc.next = pa
		else:
			pc.next = pb
		self.print_result(C)

	def result13(self, A, B):
		while A.next:
			s = A.next  # A链的首元
			A.next = s.next  # 从A链摘下首元结点s
			pre = B
			p = B.next
			while p and p.data < s.data:
				pre = p
				p = p.next
			if p is None or p.data > s.data:
				s.next = p
				pre.next = s
		self.print_result(B)


if __name__ == '__main__':
	link = MyLinkList()
	list_a = [1, 3, 4, 4, 6, 7, 8, 9]
	list_b = [4, 5, 6]
	Head = link.create(list_a)  # 返回的是链表的头结点

	# from table2 import MyLinkList as Link_List
	# link2 = Link_List()
	# Head2 = link2.create(list_b)

	# link.result1(Head)
	# link.result2(Head)
	# link.result3(Head)
	# link.result4(Head)
	# link.result5(Head)
	# print(link.result6(Head))
	# print(link.result7(Head, Head2))
	# link.result8(Head, 3, 7)
	# link.result9(Head, 3, 7)
	# link.result10(Head)
	# link.result11(Head)
	# link.result12(Head, Head2)
	link.result13(Head, Head2)
