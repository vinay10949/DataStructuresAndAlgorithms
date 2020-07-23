import sys
class node: 

    def __init__(self, info): 
        self.info = info  
        self.next = None 


class LinkedList: 

    def __init__(self): 
        self.head = None


    def display(self):
        temp = self.head 
        while (temp): 
            print(temp.info)
            temp = temp.next
    
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
            
    def reverse(self):
        self.prev=None
        self.curr=self.head
        while self.curr is not None:
            self.Next=self.curr.next
            self.curr.next=self.prev
            self.prev=self.curr
            self.curr=self.Next
        self.head=self.prev
        return
def kthnode_bruteForce(llist,k,length):
    temp=llist.head
    l=length-k
    for i in range(l):
        temp=temp.next
    return temp.info

def kthnode(llist,k):
    temp1=llist.head
    temp2=llist.head
    for i in range(k):
        temp1=temp1.next
    while temp1 is not None:
        temp1=temp1.next
        temp2=temp2.next
    return temp2.info
        

if __name__=='__main__':
    llist=LinkedList()
    print("Kth node from end of linked list")
    print("enter number of nodes")
    n=int(input())
    print("enter kth value")
    k=int(input())
    for i in range(n):
        llist.insert_at_end(int(input()))
    length=llist.count()
    k_value=kthnode_bruteForce(llist,k,length)
    print("Kth value of the list bruteforce approach")
    print(k_value)
    print("Kth value of the list")
    k_value=kthnode(llist,k)
    print(k_value)
