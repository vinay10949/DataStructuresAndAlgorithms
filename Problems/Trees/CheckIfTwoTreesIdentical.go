/*
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
*/

package main

import "fmt"

type Node struct {
	Info  int
	Left  *Node
	Right *Node
}

func insert(ptr *Node, key int) *Node {

	if ptr == nil {
		ptr = &Node{Info: key}
	} else if key <= ptr.Info {
		ptr.Left = insert(ptr.Left, key)

	} else if key > ptr.Info {
		ptr.Right = insert(ptr.Right, key)
	}
	return ptr
    }

func checkIdentical(root1 *Node, root2 *Node) bool {
	if root1 == nil && root2 == nil {
		return true

	}
	if root1 != nil && root2 != nil {
		return root1.Info == root2.Info && checkIdentical(root1.Left, root2.Left) &&
			checkIdentical(root1.Right, root2.Right)

	}
	return false
}
func main() {
	var root1, root2 *Node
	root1 = insert(root1, 10)
	root1 = insert(root1, 20)
	root1 = insert(root1, 5)
	root1 = insert(root1, 30)
	root2 = insert(root2, 10)
	root2 = insert(root2, 20)
	root2 = insert(root2, 5)
	root2 = insert(root2, 30)
	if checkIdentical(root1, root2) == true {

		fmt.Println("Trees are identical")
	} else {
		print("Trees are not identical")

	}

}
