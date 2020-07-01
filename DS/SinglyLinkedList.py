class Node:
	#constructor
	def __init__(self, info, link=None):
		self.info = info
		self.link = link

class LinkedList:

	def __init__(self):
		self.head = None

	def insert_at_begining(self, info):
		#create a new node
		newNode = Node(info)
		if self.head != None:
			newNode.link = self.head
			self.head = newNode
		else:
			self.head = newNode

	def insert_at_end(self, info):
		newNode = Node(info)
		if self.head !=None:
			current = self.head
			while current.link !=None:
				current = current.link 
			current.link = newNode
		else:
			self.head = newNode

	def delete_node(self, ele):
		if self.head == None:
			print("List Empty")
			return
		if self.head.info == ele:
			temp = self.head
			self.head = temp.link 
			temp = None 
			return 
		current = self.head
		while current.link != None:
			if current.link.info == ele:
				temp = current.link 
				current.link = temp.link
				temp = None 
				return 
			current = current.link 
		print("Element is not found in our list")

	def display(self):
		if self.head == None:
			print("List Empty")
			return 
		current = self.head 
		while current !=None:
			print(current.info)
			current = current.link

	def search(self, ele):
		if self.head == None:
			print('list is empty')
			return
		current = self.head
		i=0
		while current != None:
			if current.info == ele:
				print("Element is found in list at position ",i)
				return
			current = current.link
			i=i+1

LL = LinkedList()
LL.insert_at_begining(10)
LL.insert_at_begining(5)
LL.display()
print("*******")
LL.insert_at_end(20)
LL.insert_at_end(30)
LL.display()
LL.delete_node(40)
LL.delete_node(20)
LL.display()
LL.search(30)
