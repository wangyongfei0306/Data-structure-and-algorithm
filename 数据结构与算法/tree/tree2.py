""" 平衡二叉树 """


class Solution:
	def isBalanced(self, root):
		if not root:
			return True
		return abs(self.depth(root.left) - self.depth(root.right)) <= 1 and \
			self.isBalanced(root.left) and self.isBalanced(root.right)
	
	def depth(self, root):
		if not root:
			return 0
		return max(self.depth(root.left), self.depth(root.right)) + 1 


class Solution2:
	def isBalanced(self, root):
		return self.depth(root) != -1
		
	def depth(self, root):
		if not root:
			return 0
		left = self.depth(root.left)
		if left == -1: return -1
		right = self.depth(root.right)
		if right == -1: return -1
		return max(left, right) + 1 if abs(left - right) < 2 else -1


""" 最小的度 """
import collections


class Solution3:
	def minDepth(self, root):
		if not root:
			return 0
		de = collections.deque()
		de.append((root, 1))
		while de:
			p, dep = de.popleft()
			if not p.left and not p.right:
				return dep
			if p.left:
				de.append((p.left, dep+1))
			if p.right:
				de.append((p.right, dep+1))


""" 二叉树的最大深度 """


class Solution4:
	def maxDepth(self, root):
		stack = []
		if root is not None:
			stack.append((1, root))
		
		depth = 0
		while stack != []:
			current_depth, root = stack.pop()
			if root is not None:
				depth = max(depth, current_depth)
				stack.append((current_depth + 1, root.left))
				stack.append((current_depth + 1, root.right))
		return depth
		
		
class Solution5:
	def maxDepth(self, root):
		if not root:
			return 0
		stack = [(1, root)]
		depth = 0
		while stack:
			current_depth, node = stack.pop()
			if node:
				depth = max(depth, current_depth)
				stack.append((current_depth + 1, node.left))
				stack.append((current_depth + 1, node.right))
		return depth
		

""" 二叉树的层次遍历 """
class Solution6:
	def levelOrderBottom(self, root):
		if not root:
			return []
		queue = collections.deque()
		queue.appendleft(root)
		res = []
		while queue:
			tmp = []
			n = len(queue)
			for _ in range(n):
				node = queue.pop()
				tmp.append(node.val)
				if node.left:
					queue.appendleft(node.left)
				if node.right:
					queue.appendleft(node.right)
			res.insert(0, tmp)
		return res
		
		
class Solution7:
	def levelOrderBottom(self, root):
		queue = []                                                     # 结果列表
		cur = [root]                                                   # 接下来要循环的当前层结点，存的是结点
		while cur:                                                     # 当前层存在结点时
			cur_layer_val = []                                         # 初始化当前层结果列表为空，存的是val
			next_layer_node = []                                       # 初始化下一层结点列表为空
			for node in cur:                                           # 遍历当前层的每一个结点
				if node:                                               # 如果该结点不为空，则进行记录
					cur_layer_val.append(node.val)                     # 将该结点的值加入当前层结果列表的末尾
					next_layer_node.extend([node.left, node.right])    # 将该结点的左右孩子结点加入到下一层结点列表
			if cur_layer_val:                                          # 只要当前层结果列表不为空
				queue.insert(0, cur_layer_val)                         # 则把当前层结果列表插入到队列首端
			cur = next_layer_node                                      # 下一层的结点变为当前层，接着循环
		return queue                                                   # 返回队列结果
		
		
""" 二叉树的所有路径 """
class Solution8:
	def binaryTreePaths(self, root):
		def construct_paths(root, path):
			if root:
				path = path + str(root.val)
				if not root.left and not root.right:
					paths.append(path)
				else:
					path = path + '->'
					construct_paths(root.left, path)
					construct_paths(root.right, path)
		paths = []
		construct_paths(root, '')
		return paths
		
		
class Solution9:
	def help(self, root):
		if not root:
			return []
		paths = []
		stack = [(root, str(root.val))]
		while stack:
			root, path = stack.pop(0)
			if not root.left and not root.right:
				paths.append(path)
			if root.left:
				stack.append((root.left, path + '->' + str(root.left.val)))
			if root.right:
				stack.append((root.right, path + '->' + str(root.right.val)))
		return paths


""" 二叉树创建字符串 """


class Solution10:
	def tree2str(self, t) -> str:
		if t is None:
			return ""
		res = str(t.val)
		if t.left:
			res += '('
			res += self.tree2str(t.left)
			res += ')'
			if t.right:
				res += '('
				res += self.tree2str(t.right)
				res += ')'
		else:
			if t.right:
				res += '()('
				res += self.tree2str(t.right)
				res += ')'
		return res


class Solution11:
	def tree2str(self, t):
		if t is None:
			return ''
		if not t.left and not t.right:
			return str(t.val)
		if t.right is None:
			return t.val + '(' + self.tree2str(t.left) + ')'
		return t.val + '(' + self.tree2str(t.left) + ')(' + self.tree2str(t.right) + ')'
		
		
""" 合并二叉树 """


class Solution12:
	def mergeTrees(self, t1, t2):
		if t1 is None:
			return t2
		if t2 is None:
			return t1
		root = TreeNode(t1.val + t2.val)
		root.left = self.mergeTrees(t1.left, t2.left)
		root.right = self.mergeTrees(t1.right, t2.right)
		return root