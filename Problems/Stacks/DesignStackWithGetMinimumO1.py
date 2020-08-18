'''
Problem Statement:
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.




push(x) -- Push element x onto stack.

pop() -- Removes the element on top of the stack.

top() -- Get the top element.

getMin() -- Retrieve the minimum element in the stack.



Example 1:





Input

["MinStack","push","push","push","getMin","pop","top","getMin"]

[[],[-2],[0],[-3],[],[],[],[]]



Output

[null,null,null,null,-3,null,0,-2]



Explanation

MinStack minStack = new MinStack();

minStack.push(-2);

minStack.push(0);

minStack.push(-3);

minStack.getMin(); // return -3

minStack.pop();

minStack.top();    // return 0

minStack.getMin(); // return -2



Constraints:




Methods pop, top and getMin operations will always be called on non-empty stacks.



'''
import sys
class node: 

    def __init__(self, info): 
        self.info = info  
        self.next = None 


class Stack: 

    def __init__(self): 
        self.top = None
        self.minimum=None
        
    
    def isEmpty(self):
        if self.top is None:
            return True
        return False
    def getMin(self): 
        if self.top is None: 
            return "Stack is empty"
        else: 
            print("Minimum Element in the stack is: {}" .format(self.minimum)) 
    def push(self,data):
        if self.top==None:
            self.top=node(data)
            self.minimum=data
        
        elif data < self.minimum: 
            temp = (2 * data) - self.minimum 
            new_node = node(temp) 
            new_node.next = self.top 
            self.top = new_node 
            self.minimum = data 
        else: 
            new_node = node(data) 
            new_node.next = self.top 
            self.top = new_node 
    def pop(self):
        if self.isEmpty():
            print("Stack Underflow")
            sys.exit(0)
        temp = self.top.info 
        self.top = self.top.next
        if temp < self.minimum: 
            value=self.minimum
            self.minimum = ( ( 2 * self.minimum ) - temp ) 
            return value
        else:
            return temp
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
        while self.p is not None:
            print(self.p.info)
            self.p=self.p.next
            
if __name__=='__main__':
    stack=Stack()
    stack.push(0)
    stack.push(25)
    stack.push(5)
    stack.getMin()
    ele=stack.pop()
    print("poped Element in the stack is: {}" .format(ele))
    stack.push(-1)
    stack.getMin()



