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

func splitLinkedList2Halves(l *CircularLinkedList) (*CircularLinkedList,*CircularLinkedList){
    firstLinkedList:=&CircularLinkedList{}
    secondLinkedList:=&CircularLinkedList{}

    if l.head==nil{
        return nil,nil
    }
    slowPtr:=l.head
    fastPtr:=l.head
    for slowPtr.Next!=l.head && fastPtr.Next.Next!=l.head{
        slowPtr=slowPtr.Next
        fastPtr=fastPtr.Next.Next
    }
    fmt.Println(slowPtr.Data,fastPtr.Data," AAA")
    if fastPtr.Next.Next==l.head{
        fastPtr=fastPtr.Next
    }
    temp1:=l.head
    temp2:=l.head.Next.Next
    if l.head.Next != l.head{
        temp2 = slowPtr.Next
    }
    fastPtr.Next=slowPtr.Next
    slowPtr.Next=l.head
    firstLinkedList.head=temp1
    secondLinkedList.head=temp2
    return firstLinkedList,secondLinkedList

}

func main(){

    var l CircularLinkedList
    l.InsertAtEnd(12)
    l.InsertAtEnd(14)
    l.InsertAtEnd(16)
    l.InsertAtEnd(18)
    l.InsertAtEnd(81)
    l.InsertAtEnd(19)
    l.InsertAtEnd(91)

    l.display()
    first,second:=splitLinkedList2Halves(&l)
    fmt.Println("==============================")
    first.display()
    fmt.Println("==============================")
    second.display()
    fmt.Println("==============================")
}