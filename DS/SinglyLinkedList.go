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



type LinkedList struct {
	head  *Node
}

func (l *LinkedList) InsertAtBeginning(i int)error{
	if l==nil{
		return errors.New(" LinkedList Not initialzed")
	}
	data:=New(i)
	if l.head!=nil{
		temp:=l.head
		l.head=data
		data.Next=temp
	}else{
		l.head=data
	}
	return nil
}

func (l *LinkedList) InsertAtEnd(i int)error{
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

func (l *LinkedList) DeleteNode(i int)error{
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
	for data.Next!=nil{
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

func (l *LinkedList) Search(i int)error{
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


func (l *LinkedList) display()error{
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

	var l LinkedList
	l.InsertAtBeginning(12)
	l.InsertAtBeginning(14)
	l.InsertAtBeginning(16)
	l.InsertAtEnd(18)
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
	l.Search(18)

}
