'''
Problem Statement:
Given a singly linked list, determine if it is a palindrome.



Example 1:





Input: 1->2

Output: false


Example 2:





Input: 1->2->2->1

Output: true


Follow up:

Could you do it in O(n) time and O(1) space?


'''

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
            
def reverse(head):
    prev=None
    curr=head
    while curr is not None:
        Next=curr.next
        curr.next=prev
        prev=curr
        curr=Next
    head=prev
    return head
def display(head):
    temp =head 
    while (temp): 
        print(temp.info)
        temp = temp.next    

def isPalindrome(llist):
    head=llist.head
    slowptr=head
    fastptr=head
    slow_prev=None
    nextHalf=None
    midnode=None
    
    if head is not None and head.next is not None:
        
        while fastptr is not None and fastptr.next is not None:
            fastptr=fastptr.next.next
            slow_prev=slowptr
            slowptr=slowptr.next
            
        if fastptr is not None:
            midnode=slowptr
            slowptr=slowptr.next
        
        nextHalf=slowptr
        slow_prev.next=None
        nextHalf=reverse(nextHalf)
        res=compareList(head,nextHalf)
        nextHalf=reverse(nextHalf)
        
        if midnode is not None:
            slow_prev.next=midnode
            midnode.next=nextHalf
        else:
            slow_prev.next=nextHalf
    return res
        
def compareList(head1,head2):
    while head1 is not None and head2 is not None:
        if head1.info==head2.info:
            head1=head1.next
            head2=head2.next
        else:
            return False
    
    if head1 is None and head2 is None:
        return True
    else:
        return False

if __name__=='__main__':
    llist=LinkedList()
    n=int(input())
    for i in range(n):
        llist.insert_at_end((input()))
    if isPalindrome(llist) is True:
        print("palindrome")
    else:
        print("Not palindrome")
