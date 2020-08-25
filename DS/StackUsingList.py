import sys
class Stack:

    def __init__(self):
        self.stack=[None] * 100
        self.top=-1
    def isFull(self):
        if self.top==100:
            return True
        return False

    def isEmpty(self):
        if self.top==-1:
            return True
        return False

    def push(self,data):
        if self.isFull():
            print("stack overflow")
            return
        self.top+=1
        self.stack[self.top]=data
    def pop(self):
        if self.isEmpty():
            print("Stack Underflow")
            sys.exit(0)
        d=self.stack[self.top]
        self.top-=1
        return d
    def peek(self):
        if self.isEmpty():
            print("Stack Underflow")
            sys.exit(0)
        d=self.stack[self.top]
        return d
    def display(self):
        if self.isEmpty():
            print("Stack Underflow")
            sys.exit(0)
        self.temp=self.top
        while self.temp>=0:
            print(self.stack[self.temp])
            self.temp-=1



if __name__=='__main__':

    s=Stack()
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


