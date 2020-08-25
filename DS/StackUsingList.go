package main

import (
	"fmt"
)

type Stack struct {
	stack [100]int
	top   int
}

func NewStack()*Stack{
    var i [100]int
    s:=Stack{stack: i ,top :-1}
    return &s
}
func (s *Stack) isFull() bool {
	if s.top == len(s.stack)-1 {
		return true
	}
	return false
}

func (s *Stack) isEmpty() bool {
    if s.top == -1 {
        return true
    }
    return false
}

func (s *Stack) push(i int )  {
    if s.isFull() == true {
        fmt.Println("Stack overflow")
        return
    }
    s.top=s.top+1
    s.stack[s.top]=i
    return
}


func (s *Stack) pop() int {
    if s.isEmpty() == true {
        fmt.Println("Stack underflow")
        return -1
    }
    d:=s.stack[s.top]
    s.top=s.top-1
    return d

}
func (s *Stack) peek() int {
	if s.isEmpty() == true {
		fmt.Println("Stack underflow")
		return -1
	}
	d:=s.stack[s.top]
	return d

}

func (s *Stack) display() {
	if s.isEmpty() == true {
		fmt.Println("Stack underflow")
		return
	}
	temp:=s.top
	for temp>0{
		fmt.Println(" Element ",s.stack[temp])
		temp-=1
	}

}




func main() {
	fmt.Println("Implementing using Stack using List ")
    s:=NewStack()
    fmt.Println("Empty Stack ",s.isEmpty())
    fmt.Println("Full Stack ",s.isFull())

    for i:=0; i<120; i++{
        s.push(i)
    }

	s.display()
    for i:=0; i<120; i++{
        fmt.Println("Number " ,s.pop())
    }
	fmt.Println(" PEEK ",s.peek())
	s.display()
}


