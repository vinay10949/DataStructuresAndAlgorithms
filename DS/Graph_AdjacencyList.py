class Node:
    def __init__(self,v):
        self.vertex=v
        self.next=None

class Graph:
	#initialize matrix
	def __init__(self, size):
		self.V=size
		self.graph = [None]*size

	def add_edge(self,s,d):
		if s==d:
			print("Both vertices are same")
			return
		node=Node(d)
		node.next=self.graph[s]
		self.graph[s]=node

		node=Node(s)
		node.next=self.graph[d]
		self.graph[d]=node

	def print_graph(self):
		for row in self.graph:
			for i in range(self.V):
				temp=self.graph[i]
				while temp:
					print(temp.vertex)
					temp=temp.next
					print("\n")

g = Graph(3)
g.add_edge(0, 1)
g.print_graph()






