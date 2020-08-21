package main

import (
	"errors"
	"fmt"
)


type Node struct{
	Data int
	Next  *Node
}

func New(i int) *Node{
	n:=Node{Data: i,Next: nil}
	return &n
}



type CircularLinkedList struct {
	head  *Node
}

func (l *CircularLinkedList) InsertAtBeginning(i int)error{
	if l==nil{
		return errors.New(" LinkedList Not initialzed")
	}
	data:=New(i)
	if l.head!=nil{
		temp:=l.head
		newData:=l.head
		for newData.Next.Data!=l.head.Data{
			newData=newData.Next
		}
		newData.Next=data
		l.head=data
		l.head.Next=temp
	}else{
		l.head=data
		l.head.Next=l.head
	}
	return nil
}

func (l *CircularLinkedList) InsertAtEnd(i int)error{
	if l==nil{
		return errors.New(" LinkedList Not initialzed")
	}
	data:=New(i)
	if l.head!=nil{
		temp:=l.head
		for temp.Next!=l.head{
			temp=temp.Next
		}
		data.Next=l.head
		temp.Next=data

	}else{
		l.head=data
		l.head.Next=l.head
	}
	return nil
}

func (l *CircularLinkedList) DeleteNode(i int)error{
	if l==nil{
		return errors.New(" LinkedList Not initialzed")
	}
	if l.head==nil{
		return errors.New(" LinkedList Empty")
	}
	if l.head.Data==i{
		fmt.Println("Deleting Data from Head ",l.head.Data)
		l.head=nil
		return nil
	}
	data:=l.head
	for data.Next!=l.head{
		if data.Next.Data==i{
			temp:=data.Next
			data.Next=temp.Next
			temp=nil
			return nil
		}
		data=data.Next
	}
	fmt.Println("Element not found in list ")
	return nil
}

func (l *CircularLinkedList) Search(i int)error{
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
	for data.Next!=l.head{
		if data.Next.Data==i{
			fmt.Println("Element Found ")
			return nil
		}
		data=data.Next
	}
	fmt.Println("Element not found in list ")
	return nil
}


func (l *CircularLinkedList) display()error{
	if l==nil{
		return errors.New(" LinkedList Not initialzed")
	}

	if l.head!=nil{
		fmt.Println(l.head.Data)
		data:=l.head.Next
		for data.Data!=l.head.Data{
			fmt.Println(data.Data)
			data=data.Next
		}
	}else{
		errors.New(" LinkedList Empty")
	}
	return nil
}


func main(){

	var l CircularLinkedList
	l.InsertAtBeginning(12)
	l.InsertAtBeginning(14)
	l.InsertAtBeginning(16)
	l.InsertAtBeginning(18)
	l.InsertAtEnd(28)
	fmt.Println("Deleting node ",14)
	l.DeleteNode(14)

	err:=l.display()
	if err!=nil{
		fmt.Println(err)
	}
	fmt.Println("Searching Node 18 ")
	l.Search(18)
	fmt.Println("Searching Node 15 ")
	l.Search(15)

	}
