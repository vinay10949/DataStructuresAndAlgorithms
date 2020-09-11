package main

import "fmt"

type Node struct{
    Info int
    Next  *Node
}

type Queue struct{
    Front *Node
    Rear *Node
}

func New()*Queue{
    q:=Queue{nil,nil}
    return &q
}

func(q * Queue) isEmpty()bool{
    return q.Front==nil
}


func(q * Queue) EnQueue(i int ){

    n:=Node{Info: i}
    if q.Front==nil{
        q.Front=&n
        q.Rear=&n
    }
    temp:=q.Rear
    temp.Next=&n
    q.Rear=&n

}

func(q * Queue) DeQueue() int {
    if q.isEmpty(){
        return -1
    }
    temp:=q.Front
    q.Front=temp.Next
    if q.Front==nil{
        q.Rear=nil
    }
    return temp.Info
}

func(q * Queue) Display()  {
    if q.isEmpty(){
        return
    }
    p:=q.Front
    for p!=nil{
        fmt.Println(p.Info)
        p=p.Next
    }
}

func main(){

    q:=New()
    q.EnQueue(10)
    q.EnQueue(10)
    q.EnQueue(100)
    q.EnQueue(70)
    q.Display()
    fmt.Println("******************")
    fmt.Println(q.DeQueue())
    fmt.Println(q.DeQueue())
    fmt.Println("******************")
    q.Display()

}
                

