'''
Problem Statement:

Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL

Output: 5->4->3->2->1->NULL

'''

class Node:
	#constructor
	def __init__(self, info, link=None):
		self.info = info
		self.link = link

class LinkedList:

	def __init__(self):
		self.head = None

	def insert_at_end(self, info):
		newNode = Node(info)
		if self.head !=None:
			current = self.head
			while current.link !=None:
				current = current.link 
			current.link = newNode
		else:
			self.head = newNode


	def display(self):
		if self.head == None:
			print("List Empty")
			return 
		current = self.head 
		while current !=None:
			print(current.info)
			current = current.link

	def reverse(self):
		if self.head == None:
			print("List Empty")
			return 
		prev=None
		current = self.head 
		next=None
		while current !=None:
			next=current.link
			print("NEXT " ,next.info)
			current.link=prev
			print("CURRENT " ,current.link.info)
			prev=current
			current =next
		self.head=prev
		return 

LL = LinkedList()
LL.insert_at_end(20)
LL.insert_at_end(30)
LL.insert_at_end(50)
LL.insert_at_end(10)
LL.insert_at_end(80)
LL.display()
print("====================================")
print("Reversing LinkedList")
LL.reverse()	
LL.display()
