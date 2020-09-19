'''


Problem Statement:

Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:

In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example:

Input:


    1

   / \

  2   3

 / \  /

4  5 6

Output: 6

Level: Medium




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


def countNodes(root):
    if root==None:
        return 0
    return (1+countNodes(root.left)+countNodes(root.right))

if __name__=='__main__':
    root=None
    root=insert(root,10)
    root=insert(root,20)
    root=insert(root,5)
    root=insert(root,30)
    print(countNodes(root))
