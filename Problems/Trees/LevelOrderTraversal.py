'''
Problem Statement:

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:

Given binary tree [3,9,20,null,null,15,7],

3

/ \

9 20

/ \

15 7

return its level order traversal as:

[

[3],

[9,20],

[15,7]


]

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

def levelOrderTraversal(root):
    if root==None:
        return 
    queue=[]
    
    queue.append(root)
    while(len(queue)>0):
        print(queue[0].info)
        Node=queue.pop(0)
        
        if(Node.left is not None):
            queue.append(Node.left)
        if(Node.right is not None):
            queue.append(Node.right)

if __name__=='__main__':
    root=None
    root=insert(root,10)
    root=insert(root,20)
    root=insert(root,15)
    root=insert(root,30)
    levelOrderTraversal(root)

