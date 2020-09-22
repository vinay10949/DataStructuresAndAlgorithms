'''
Problem Statement:

Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

 Input: 1 1


   / \ / \


  2 3 2 3

[1,2,3], [1,2,3]

Output: true

Example 2:

Input: 1 1

  / \


  2 2

[1,2], [1,null,2]

Output: false


Level: Easy
'''
import sys
class node: 

    def __init__(self, info): 
        self.info = info  
        self.left = None
        self.right = None 
    
def insert(ptr,key):
    if(ptr is None):
        ptr=node(key)
    elif(key<=ptr.info):
        ptr.left=insert(ptr.left,key)
    elif(key>ptr.info):
        ptr.right=insert(ptr.right,key)
    return ptr
def inorder(ptr):
    if(ptr==None):
        return
    inorder(ptr.left)
    print(ptr.info)
    inorder(ptr.right)
    
def checkIdentical(root1,root2):
    if root1 is None and root2 is None:
        return True
    if root1 is not None and root2 is not None:
        return root1.info==root2.info and checkIdentical(root1.left,root2.left) and checkIdentical(root1.right,root2.right)
    return False
if __name__=='__main__':
    root1=None
    root2=None
    root1=insert(root1,10)
    root1=insert(root1,20)
    root1=insert(root1,5)
    root1=insert(root1,30)
    root2=insert(root2,10)
    root2=insert(root2,20)
    root2=insert(root2,5)
    root2=insert(root2,30)
    if checkIdentical(root1,root2) is True:
        print("Trees are identical")
    else:
        print("Trees are not identical")

