class Node:
    def __init__(self,info,next=None):
        self.info=info
        self.next=next

class Queue:
    def __init__(self):
        self.front=self.rear=None

    def isEmpty(self):
        return self.front==None
    
    def EnQueue(self,ele):
        n=Node(ele)
        if self.isEmpty():
            self.front=self.rear=n
            return 
        self.rear.next=n
        self.rear=n
        
    def DeQueue(self):
        if self.isEmpty():
            print("Queue is Empty ")
            return
        temp=self.front
        self.front=temp.next
        if self.front==None:
            self.rear=None    
        return temp

    def display(self):
        p=self.front
        while p!=None:
            print(p.info)
            p=p.next 
q=Queue()
q.EnQueue(10)
q.EnQueue(10)
q.EnQueue(100)
q.EnQueue(70)
print(q.display())
print("******************")
print(q.DeQueue())
print(q.DeQueue())
print(q.display())
                

