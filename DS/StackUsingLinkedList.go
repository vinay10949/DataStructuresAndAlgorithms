package main

import (
    "fmt"
)

type Node struct {
    Val   int
    Next   *Node
}
type Stack struct {
    top   *Node
}

func NewStack()*Stack{
    s:=Stack{top :nil}
    return &s
}
func NewNode(i int)*Node{
    return &Node{Val:i}
}

func (s *Stack) isEmpty() bool {
    if s.top == nil {
        return true
    }
    return false
}


func (s *Stack) push(i int )  {
    temp:=NewNode(i)
    nodeTemp:=s.top
    s.top=temp
    if s.isEmpty() == true {
        fmt.Println("Stack underflow")
        return
    }

    temp.Next=nodeTemp
}



func (s *Stack) pop() int {
    if s.isEmpty() == true {
        fmt.Println("Stack underflow")
        return -1
    }
    d:=s.top
    s.top=s.top.Next
    return d.Val

}


func (s *Stack) peek() int {
    if s.isEmpty() == true {
        fmt.Println("Stack underflow")
        return -1
    }

    return s.top.Val

}

func (s *Stack) display() {
    if s.isEmpty() == true {
        fmt.Println("Stack underflow")
        return
    }
    temp:=s.top
    for temp!=nil{
        fmt.Println(" Element ",temp.Val)
        temp=temp.Next
    }

}




func main() {
    fmt.Println("Implementing using Stack using List ")
    s:=NewStack()
    fmt.Println("Empty Stack ",s.isEmpty())
    for i:=0;i<10;i++{
        s.push(i)

    }

    fmt.Println("PEEK ",s.peek())

    for i:=0;i<10;i++{
       fmt.Println(s.pop())

    }

    s.display()
}


