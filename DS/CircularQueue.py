class Node:
    def __init__(self,info,next=None):
        self.info=info
        self.next=next

class CircularQueue:
    def __init__(self):
        self.front=self.rear=None

    def isEmpty(self):
        return self.front==None
    
    def EnQueue(self,ele):
        temp=Node(ele)
        if self.isEmpty():
            self.front=temp
        else:
            self.rear.next=temp
        self.rear=temp
        self.rear.next=self.front
        

    def DeQueue(self):
        if self.isEmpty():
            print("Queue is Empty ")
            return -1
        temp=self.front
        if self.rear==self.front:
            self.front=self.rear=None
        else:
            self.front=temp.next
            self.rear.next=self.front 
        return temp.info

    def display(self):
        p=self.front
        while p.next!=self.front:
            print(p.info)
            p=p.next    
        print(p.info)
        

q=CircularQueue()
q.EnQueue(10)
q.EnQueue(10)
q.EnQueue(100)
q.EnQueue(70)
q.EnQueue(120)
print(q.display())
print("******************")
q.DeQueue()
q.DeQueue()
print(q.display())
                

