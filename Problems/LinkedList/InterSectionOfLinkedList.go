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

	var l1,l2 LinkedList

	l1.InsertAtEnd(10)
	l1.InsertAtEnd(12)
	l1.InsertAtEnd(1)
	l1.InsertAtEnd(9)
	l1.InsertAtEnd(6)



    l2.InsertAtEnd(16)
    l2.InsertAtEnd(2)
    l2.InsertAtEnd(15)
	l1.display()
	fmt.Println("===================")
	l2.display()


	//Merging
    temp1:=l1.head
    temp2:=l2.head
    for temp2.Next!=nil{
        temp2=temp2.Next
    }
    temp2.Next=temp1.Next.Next.Next
    temp2=l2.head
    l3:=LinkedList{temp1}
    l4:=LinkedList{temp2}
    fmt.Println("Merged List1")

    for temp1!=nil{
        fmt.Println("Temp 1 ",temp1.Data)
        temp1=temp1.Next
    }
    fmt.Println("Merged List2")
    for temp2!=nil{
        fmt.Println("Temp 2 ",temp2.Data)
        temp2=temp2.Next
    }
	l1Count:=l3.getCount()
	l2Count:=l4.getCount()
	d:=0
	if l1Count>l2Count{
	    d:=l1Count-l2Count
        fmt.Println("Intersection of 2 List ",getInterSection(l1.head,l2.head,d))
    }else{
        d=l2Count-l1Count
        fmt.Println("Intersection of 2 List ",getInterSection(l2.head,l1.head,d))
    }

}

func getInterSection(l1 *Node ,l2 *Node,d int )int{
    for d>0{
        l1=l1.Next
        d=d-1
    }
    for l1.Next!=nil && l2.Next!=nil{
        fmt.Println(l1.Data,l2.Data)
        if l1.Data==l2.Data{
            return l1.Data
        }
        l1=l1.Next
        l2=l2.Next
    }

    return 0
}
