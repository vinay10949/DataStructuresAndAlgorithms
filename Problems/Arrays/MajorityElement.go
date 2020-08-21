package main

import (
    "fmt"
)

func main(){

    arr:=[]int{1,3,2,2,2,5,6,2,2}
    fmt.Println("Given Array ",arr)
    fmt.Println("Find majority element in an array using O(1) Space and O(n) time complexity")

    count:=1
    majorityElement:=0
    for _,i :=range arr{
        if i==majorityElement{
            count=count+1
        }else{
            count=count-1
        }
        if count==0{
            majorityElement=i
            count=count+1

        }
    }
    mCount:=0
    for _,i :=range arr{
        if i==majorityElement{
            mCount+=1
        }
    }
    if mCount>len(arr)/2{
        fmt.Println("Majority Element Found ",majorityElement)
    }else{
        fmt.Println("Majority Element not found ")
    }

}