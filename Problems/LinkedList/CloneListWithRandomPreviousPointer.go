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

func cloneLinkedList(l *DoublyLinkedList) *DoublyLinkedList{
    tmp:=l.head
    for tmp!=nil{
        newNode:=New(tmp.Data)
        newNode.Next=tmp.Next
        tmp.Next=newNode
        tmp=tmp.Next.Next
    }
    tmp=l.head
    for tmp!=nil{
      tmp.Next.Prev=tmp.Prev.Next
      tmp=tmp.Next.Next
    }

    tmp=l.head
    dup_root := tmp.Next
    for tmp.Next!=nil{
        curr:=tmp.Next
        curr.Next=curr.Next.Next
        curr=tmp
    }
    return &DoublyLinkedList{dup_root}
}

func main(){

    var l DoublyLinkedList
    l.InsertAtEnd(12)
    l.InsertAtEnd(14)
    l.InsertAtEnd(16)
    l.InsertAtEnd(18)
    l.InsertAtEnd(20)
    l.InsertAtEnd(40)

    l.head.Prev = l.head.Next.Next
    fmt.Println()
    l.head.Next.Prev = l.head
    fmt.Printf(" %d --->%d", l.head.Next.Prev.Data , l.head.Data)
    fmt.Println()
    l.head.Next.Next.Next = l.head.Next.Next.Next.Next
    fmt.Printf(" %d --->%d", l.head.Next.Next.Next.Data , l.head.Next.Next.Next.Next.Data)
    fmt.Println()
    l.head.Next.Next.Next.Prev = l.head.Next.Next.Next.Next
    fmt.Printf(" %d --->%d", l.head.Next.Next.Next.Prev.Data , l.head.Next.Next.Next.Next.Data)
    fmt.Println()
    l.head.Next.Next.Next.Next.Prev = l.head.Next
    fmt.Printf(" %d --->%d", l.head.Next.Next.Next.Next.Prev.Data, l.head.Next.Data)
    fmt.Println()
    fmt.Println("original list")
    l.display()
    fmt.Println("=====================================")
    fmt.Println("=====================================")
    copyList:=cloneLinkedList(&l)
    copyList.display()


}
