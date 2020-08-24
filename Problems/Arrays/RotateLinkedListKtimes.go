package main

import "fmt"

  type ListNode struct {
      Val int
      Next *ListNode
  }


func getCount(head *ListNode)int{
    d:=head
    count:=0
    for d.Next!=nil{
        count=count+1
        d=d.Next
    }
    return count+1
}


//Time Complexity O(n) Space Complexity O(1)

func rotateRight(head *ListNode, k int) *ListNode {
    cnt:=getCount(head)
    fmt.Println("Count ",cnt)
    if k>=cnt{
        k=k-cnt
    }
    data:=head
    temp:=data
    i:=k
    for i>0{
        temp=temp.Next
        i=i-1
    }
    count:=0
    for temp.Next!=nil{
        data=data.Next
        temp=temp.Next
        count=count+1
    }
    temp.Next=head
    head=data.Next
    data.Next=nil

    return head

}

func main(){
    l:=ListNode{0,&ListNode{1,&ListNode{2,nil}}}
    d:=rotateRight(&l,5)
    fmt.Print(d.Val," ",d.Next.Val," ",d.Next.Next.Val)


}