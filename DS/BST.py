#Inorder Traversal with out recursion 

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
		#set current to root of binary search tree
		current = root
		stack = []

		while True:
			# reach the left most node of the current root
			if current is not None:
				stack.append(current)
				current = current.left
			elif stack:
				current = stack.pop()
				print(current.data)
				current = current.right
			else:
				break

        
	def inorderR(self, root):
		#set current to root of binary search tree
		self.inorder(root.left)
		print(root.data)
		self.inorder(root.right)

        
	def preorder(self, root):
		#set current to root of binary search tree
		print(root.data)
		self.inorder(root.left)
		self.inorder(root.right)

	def min(self, root):
    		#set current to root of binary search tree
		current=root
		while current.left is not None :
    			current=current.left
		return current.data

	def max(self, root):
    		#set current to root of binary search tree
		current=root
		while current.right is not None :
    			current=current.right
		return current.data

	def search(self, root,ele):
    		#set current to root of binary search tree
		if root is None or root.data==ele:
    			return root.data
		if root.data<ele:
			return self.search(root.right,ele)
		return self.search(root.left,ele)

root = None
b = BST()
for ele in [10, 5, 25, 2, 7, 30]:
	root = b.buildBst(root, ele)
#b.inorder(root)
#b.inorderR(root)
print(b.min(root))

print(b.max(root))
print(b.search(root,7))
print("===============")
print(b.preorder(root))
