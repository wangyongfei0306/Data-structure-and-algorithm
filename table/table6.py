class Node:
	def __init__(self, data=None):
		self.data = data
		self.next = None


class MyLinkList:
	def __init__(self):
		self.head = Node(-1)

	""" 循环链表 """
	def create(self, list_a):
		rear = self.head
		self.head.next = self.head
		for i in range(len(list_a)):
			node = Node(list_a[i])
			node.next = rear.next
			rear.next = node
			rear = node
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
		while p and p.data != -1:
			res.append(str(p.data))
			p = p.next
		print('->'.join(res))

	@staticmethod
	def result1(head_a):
		""" 计算链表长度 """
		p, count = head_a, 0
		while p.next != head_a:
			p = p.next
			count += 1
		return count

	def result2(self, head_a, x):
		""" 查找指定值的位置 """
		index = 1
		pre = head_a
		p = pre.next
		while p != pre:
			if p.data == x:
				print(index, end=' ')
			index += 1
			p = p.next


if __name__ == '__main__':
	list_a = [1, 3, 4, 6, 7, 9]
	list_b = [7, 6, 4]
	link = MyLinkList()
	head = link.create(list_a)

	# print(link.result1(head))
	link.result2(head, 4)



