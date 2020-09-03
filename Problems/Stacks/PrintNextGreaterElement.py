'''
****************************************************************************************************

Problem Statement:

You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.

Example 1:





Input: nums1 = [4,1,2], nums2 = [1,3,4,2].

Output: [-1,3,-1]

Explanation:

    For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.

    For number 1 in the first array, the next greater number for it in the second array is 3.

    For number 2 in the first array, there is no next greater number for it in the second array, so output -1.

Example 2:

Input: nums1 = [2,4], nums2 = [1,2,3,4].

Output: [3,-1]

Explanation:

    For number 2 in the first array, the next greater number for it in the second array is 3.

    For number 4 in the first array, there is no next greater number for it in the second array, so output -1.

Note:
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

def nextGreaterEle(arr,n):
    s=Stack()
    s.push(arr[0])
    for i in range(1,n):
        temp=arr[i]
        if s.isEmpty() is not True:
            element=s.pop()
            while(element<temp):
                print("{} -> {}".format(element,temp))
                if s.isEmpty() is True:
                    break
                element=s.pop()
            if element>temp:
                s.push(element)
        s.push(temp)

    while s.isEmpty() is not True:
        element=s.pop()
        temp=-1
        print("{} -> {}".format(element,temp))
    
if __name__=='__main__':
    arr=[4, 3, 2, 1]
    n=len(arr)
    nextGreaterEle(arr,n)



