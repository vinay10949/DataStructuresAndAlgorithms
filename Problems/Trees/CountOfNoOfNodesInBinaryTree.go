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

func countNodes(root *Node) int {
	if root == nil {
		return 0
	}
	return 1 + countNodes(root.Left) + countNodes(root.Right)

}

func main() {

	fmt.Println("Constructing binary tree ")
	var root *Node
	root = insert(root, 10)
	root = insert(root, 20)
	root = insert(root, 5)
	root = insert(root, 30)
	fmt.Println(countNodes(root))

}
