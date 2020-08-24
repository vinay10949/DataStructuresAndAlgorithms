package main

import (
    "errors"
    "fmt"
)

type Node struct {
	Data int
	Next *Node
}

func New(i int) *Node {
	n := Node{Data: i, Next: nil}
	return &n
}

type LinkedList struct {
	head *Node
}

func (l *LinkedList)getCount()int{
    count:=1
    d:=l.head
    for d.Next!=nil{
        count+=1
        d=d.Next

    }
    return count
}

func (l *LinkedList) InsertAtBeginning(i int) error {
	if l == nil {
		return errors.New(" LinkedList Not initialzed")
	}
	data := New(i)
	if l.head != nil {
		temp := l.head
		l.head = data
		data.Next = temp
	} else {
		l.head = data
	}
	return nil
}

func (l *LinkedList) InsertAtEnd(i int) error {
	if l == nil {
		return errors.New(" LinkedList Not initialzed")
	}
	data := New(i)
	if l.head != nil {
		temp := l.head
		for temp.Next != nil {
			temp = temp.Next
		}
		temp.Next = data
	} else {
		l.head = data
	}
	return nil
}

func (l *LinkedList) DeleteNode(i int) error {
	if l == nil {
		return errors.New(" LinkedList Not initialzed")
	}
	if l.head == nil {
		return errors.New(" LinkedList Empty")
	}
	if l.head.Data == i {
		fmt.Println("Deleting Data from Head ", l.head.Data)
		l.head = nil
		return nil
	}
	data := l.head
	for data.Next != nil {
		if data.Next.Data == i {
			temp := data.Next
			data.Next = temp.Next
			temp = nil
			return nil
		}
		data = data.Next
	}
	fmt.Println("Element not found in list ")
	return nil
}

func (l *LinkedList) Search(i int) error {
	if l == nil {
		return errors.New(" LinkedList Not initialzed")
	}
	if l.head == nil {
		return errors.New(" LinkedList Empty")
	}
	if l.head.Data == i {
		fmt.Println("Element Found ")
		return nil
	}
	data := l.head
	for data.Next != nil {
		if data.Next.Data == i {
			fmt.Println("Element Found ")
			return nil
		}
		data = data.Next
	}
	fmt.Println("Element not found in list ")
	return nil
}

func (l *LinkedList) display() error {
	if l == nil {
		return errors.New(" LinkedList Not initialzed")
	}

	if l.head != nil {
		data := l.head
		for data != nil {
			fmt.Println(data.Data)
			data = data.Next
		}
	} else {
		errors.New(" LinkedList Empty")
	}
	return nil
}

func main() {

	var l1 LinkedList

	l1.InsertAtEnd(10)
	l1.InsertAtEnd(1)
	l1.InsertAtEnd(9)
	l1.InsertAtEnd(6)
	l1.InsertAtEnd(7)
	l1.display()

	a:=l1.head
	b:=l1.head.Next

	var l3,l4 LinkedList
	cnt:=l1.getCount()
	for cnt>0{
		if cnt%2==0{
			fmt.Println("Second ",b.Data)
			l3.InsertAtEnd(b.Data)
			if b.Next!=nil{
				if b.Next.Next!=nil{
					b=b.Next.Next
				}
			}
		}else{
			fmt.Println("First ",a.Data)
			l4.InsertAtEnd(a.Data)
			if a.Next!=nil{
				if a.Next.Next!=nil{
					a=a.Next.Next
				}
			}
		}

		cnt=cnt-1
	}

	fmt.Println("===============================")
	l3.display()
	fmt.Println("===============================")

	l4.display()

}
