'''
**********************************************************************************

Problem Statement:

Write a class StockSpanner which collects daily price quotes for some stock, and returns the span of that stock's price for the current day.

The span of the stock's price today is defined as the maximum number of consecutive days (starting from today and going backwards) for which the price of the stock was less than or equal to today's price.

For example, if the price of a stock over the next 7 days were [100, 80, 60, 70, 60, 75, 85], then the stock spans would be [1, 1, 1, 2, 1, 4, 6].
Example 1:

Input: ["StockSpanner","next","next","next","next","next","next","next"], [[],[100],[80],[60],[70],[60],[75],[85]]

Output: [null,1,1,1,2,1,4,6]

Explanation: First, S = StockSpanner() is initialized. Then: S.next(100) is called and returns 1, S.next(80) is called and returns 1, S.next(60) is called and returns 1, S.next(70) is called and returns 2, S.next(60) is called and returns 1, S.next(75) is called and returns 4, S.next(85) is called and returns 6. Note that (for example) S.next(75) returned 4, because the last 4 prices (including today's price of 75) were less than or equal to today's price.



Note:




Calls to StockSpanner.next(int price) will have 1 <= price <= 10^5.

There will be at most 10000 calls to StockSpanner.next per test case.

There will be at most 150000 calls to StockSpanner.next across all test cases.

The total time limit for this problem has been reduced by 75% for C++, and 50% for all other languages.

'''
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
        while self.p is not None:
            print(self.p.info)
            self.p=self.p.next
def calculateSpan(price,n,stock):
    s=Stack()
    s.push(0)
    stock[0]=1
    
    for i in range(1,n):
        
        while s.isEmpty() is not True and price[s.peek()]<=price[i]:
            ele=s.pop()
        
        if s.isEmpty():
            stock[i]=i+1
        else:
            stock[i]=i-s.peek()
        
        s.push(i)
    return stock


if __name__=='__main__':
    price=[10, 4, 5, 90, 120, 80]
    n=len(price)
    stock=[0]*n
    stock=calculateSpan(price,n,stock)
    for i in stock:
        print("{} ".format(i)),

