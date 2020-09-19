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
def clone(head):
    curr = head
    while curr != None:
        new = node(curr.info)
        new.next = curr.next
        curr.next = new
        curr = curr.next.next
    curr = head
    while curr != None:
        curr.next.random = curr.random.next
        curr = curr.next.next

    curr = head
    dup_root = head.next
    while curr.next != None:
        tmp = curr.next
        curr.next = curr.next.next
        curr = tmp

    return dup_root
def print_list(head):
    temp=head
    while temp!=None:
        print('Data =', temp.info, ', Random =', temp.random.info)
        temp=temp.next

if __name__=='__main__':
    llist=LinkedList()
    for i in range(5):
        llist.insert_at_end(int(input()))
    temp=llist.head
    temp.random = temp.next.next
    temp.next.random = temp
    temp.next.next.random = temp.next.next.next.next
    temp.next.next.next.random = temp.next.next.next.next
    temp.next.next.next.next.random = temp.next
    print("original list")
    print_list(llist.head)
    cloned_list = clone(llist.head)

    print('\nCloned list:')
    print_list(cloned_list)



