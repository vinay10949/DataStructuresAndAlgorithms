class Node:
    
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

class BST:

	def buildBst(self, root, ele):
		if root == None:
			return Node(ele)
		if ele < root.data:
			root.left = self.buildBst(root.left, ele)
		else:
			root.right = self.buildBst(root.right, ele)
		return root

	def inorder(self, root):
		if root == None:
			return
		self.inorder(root.left)
		print(root.data)
		self.inorder(root.right)

	def successor(self, root):
		root = root.right
		while root.left:
			root = root.left
		return root.data

	def predecessor(self, root):
		root = root.left
		while root.right:
			root = root.right
		return root.data

	def deletion(self, root, key):
		if not root:
			return None

		if key < root.data:
			root.left = self.deletion(root.left, key)
		elif key > root.data:
			root.right = self.deletion(root.right, key)
		else:
			if not (root.left or root.right):
				root = None

			elif root.right:
				root.data = self.successor(root)
				root.right = self.deletion(root.right, root.data)

			else:
				root.data = self.predecessor(root)
				root.left = self.deletion(root.left, root.data)
		return root




root = None
b = BST()
for ele in [2, 1, 33, 0, 25, 40, 11, 34, 7, 12, 36, 13]:
	root = b.buildBst(root, ele)

b.inorder(root)
b.deletion(root, 25)
print('****')
b.inorder(root)
