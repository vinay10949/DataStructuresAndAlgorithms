import sys
class node: 

    def __init__(self, info): 
        self.info = info  
        self.next = None
        self.random=None


class LinkedList: 

    def __init__(self): 
        self.head = None


    def display(self):
        temp = self.head 
        while (temp): 
            print("{} ->".format(temp.info)),
            temp = temp.next
        print("NULL")
    
    def count(self):
        count=0
        temp=self.head
        while(temp):
            count+=1
            temp=temp.next
        return count
    
    def serach(self,value):
        temp=self.head
        pos=1
        while(temp):
            if(temp.info==value):
                print("The value found at",pos)
            temp=temp.next
            pos+=1
        print("Value not found in the linked list")
    def insert_at_beg(self,data):
        self.temp = node(data)
        if self.head is None:
            self.head = self.temp
            return
        self.temp.next = self.head
        self.head= self.temp
    def insert_at_end(self,data):
        self.temp = node(data)
        if self.head is None:
            self.head = self.temp
            return
        self.p = self.head
        while self.p.next is not None:
            self.p=self.p.next
        self.p.next = self.temp;
        
    def insert_after_given_node(self,data,item):
        self.p=self.head
        while self.p is not None:
            if(self.p.info==item):
                self.temp=node(data)
                self.temp.next=self.p.next
                self.p.next=self.temp
                return
            self.p=self.p.next
        print("Item not found")

    def insert_at_pos(self,data,pos):
        self.temp=node(data)
        if pos==1:
            self.temp.next = self.head
            self.head= self.temp
            return
        self.p=self.head
        while pos>2 and self.p is not None:
            self.p=self.p.next
            pos-=1
        if self.p is None:
            print("Position exceeded the length of the list")
        else:
            self.temp.next=self.p.next
            self.p.next=self.temp
    def delete(self,data):
        if self.head is None:
            print("List is empty")
            return
        if self.head.info==data:
            self.temp=self.head
            self.head=self.head.next
            return
        self.p=None
        self.curr=self.head
        while self.curr is not None:
            if self.curr.info==data:
                self.temp=self.p.next
                self.p.next=self.temp.next
                return
            self.p=self.curr
            self.curr=self.curr.next
def kthAlternate(head,k):
    prev=None
    curr=head
    Next=None
    count=0
    while curr is not None and count<k:
        Next=curr.next
        curr.next=prev
        prev=curr
        curr=Next
        count+=1
    if head is not None:
        head.next=curr
    count=0
    while count<k-1 and curr is not None:
        curr=curr.next
        count+=1
    if curr is not None:
        curr.next=kthAlternate(curr.next,k)
    return prev

if __name__=='__main__':
    llist=LinkedList()
    print("Enter number of elements")
    n=int(input())
    for i in range(n):
        llist.insert_at_end(int(input()))
    llist.head=kthAlternate(llist.head,3)
    llist.display()

