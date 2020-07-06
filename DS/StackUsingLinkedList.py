import sys
class node: 

    def __init__(self, info): 
        self.info = info  
        self.next = None 


class Stack: 

    def __init__(self): 
        self.top = None
        
    
    def isEmpty(self):
        if self.top is None:
            return True
        return False
    
    def push(self,data):
        self.temp=node(data)
        if self.temp is None:
            print("Stack overflow")
            return
        self.temp.next=self.top
        self.top=self.temp
    
    def pop(self):
        if self.isEmpty():
            print("Stack Underflow")
            sys.exit(0)
        d=self.top.info
        self.top=self.top.next    
        return d
    
    def peek(self):
        if self.isEmpty():
            print("Stack Underflow")
            sys.exit(0)
        d=self.top.info
        return d
    def display(self):
        if self.isEmpty():
            print("Stack Underflow")
            sys.exit(0)
        self.p=self.top
        while self.top is not None:
            print(self.p.info)
            self.p=self.p.next
            
    
        
if __name__=='__main__': 

    s = Stack()
    while(1):
        print("1.Push\n");
        print("2.Pop\n");
        print("3.Display the top element\n");
        print("4.Display all stack elements\n");
        print("5.Quit\n");
        print("Enter your choice : ");
        choice=int(input())
        if choice==1:
            value=int(input())
            s.push(value)
        elif choice==2:
            d=s.pop()
            print("poped value",d)
        elif choice==3:
            print("top of the element",s.peek())
        elif choice==4:
            s.display()
        else:
            sys.exit(0)
            
            
        


