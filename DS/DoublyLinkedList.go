package main

import (
	"errors"
	"fmt"
)


type Node struct{
	Data int
	Next  *Node
	Prev  *Node
}

func New(i int) *Node{
	n:=Node{Data: i,Next: nil,Prev: nil}
	return &n
}



type DoublyLinkedList struct {
	head  *Node
}

func (l *DoublyLinkedList) InsertAtBeginning(i int)error{
	if l==nil{
		return errors.New(" LinkedList Not initialzed")
	}
	data:=New(i)
	if l.head!=nil{
		temp:=l.head
		l.head=data
		data.Next=temp
		temp.Prev=data
	}else{
		l.head=data
	}
	return nil
}

func (l *DoublyLinkedList) InsertAtEnd(i int)error{
	if l==nil{
		return errors.New(" LinkedList Not initialzed")
	}
	data:=New(i)
	if l.head!=nil{
		temp:=l.head
		for temp.Next!=nil{
			temp=temp.Next
		}
		temp.Next=data
	}else{
		l.head=data
	}
	return nil
}

func (l *DoublyLinkedList) DeleteNode(i int)error{
	if l==nil{
		return errors.New(" LinkedList Not initialzed")
	}
	if l.head==nil{
		return errors.New(" LinkedList Empty")
	}
	if l.head.Next==nil && l.head.Data==i{
		fmt.Println("Deleting Data from Head ",l.head.Data)
		l.head=nil
		return nil
	}
	data:=l.head
	for data!=nil{
		if data.Data==i{
			data.Prev.Next=data.Next
			data.Next.Prev=data.Prev

			return nil
		}
		data=data.Next

	}
	if data.Data==i{
		data.Prev.Next=nil
	}
	fmt.Println("Element not found in list ")
	return nil
}

func (l *DoublyLinkedList) Search(i int)error{
	if l==nil{
		return errors.New(" LinkedList Not initialzed")
	}
	if l.head==nil{
		return errors.New(" LinkedList Empty")
	}
	if l.head.Data==i{
		fmt.Println("Element Found ")
		return nil
	}
	data:=l.head
	for data.Next!=nil{
		if data.Next.Data==i{
			fmt.Println("Element Found ")
			return nil
		}
		data=data.Next
	}
	fmt.Println("Element not found in list ")
	return nil
}


func (l *DoublyLinkedList) display()error{
	if l==nil{
		return errors.New(" LinkedList Not initialzed")
	}

	if l.head!=nil{
		data:=l.head
		for data!=nil{
			fmt.Println(data.Data)
			data=data.Next
		}
	}else{
		errors.New(" LinkedList Empty")
	}
	return nil
}


func main(){

	var l DoublyLinkedList
	l.InsertAtBeginning(12)
	l.InsertAtBeginning(14)
	l.InsertAtBeginning(16)
	l.InsertAtEnd(18)
	l.InsertAtEnd(20)
	err:=l.display()
	if err!=nil{
		fmt.Println(err)
	}
	fmt.Println("==================")
	fmt.Println("Deleting node ")
	l.DeleteNode(14)
	l.display()
	fmt.Println("After Deletion ")
	fmt.Println("==================")
	fmt.Println("Searching 11 ")
	l.Search(11)
	fmt.Println("==================")
	fmt.Println("Searching 16 ")
	l.Search(16)


}
