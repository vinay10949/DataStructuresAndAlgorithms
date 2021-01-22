package main

import (
	"fmt"
	"math/rand"
	"time"
)

/*
Time Complexity
Worst Case- O(n*n)
Best Case- O(n) – When the array is already sorted
Space Complexity
Space Complexity of insertion sort is O(1)


 */


func main() {

	fmt.Println("Bubble Sort Demo ")
	rand.Seed(time.Now().UnixNano())
	min := 0
	max := 100
	i := 0
	lstIntegers := make([]int, 0)
	for i <= 10 {
		lstIntegers = append(lstIntegers, rand.Intn(max-min+1)+min)
		i = i + 1
	}
	fmt.Println("Created Random list of Integers ", lstIntegers)
	fmt.Println("Sorting it by Bubble sort")
	fmt.Println("Final Sorted List ", bubbleSort(lstIntegers))
}

func bubbleSort(input []int) []int{
    // n is the number of items in our list
    n := len(input)
    // set swapped to true
    swapped := true
    // loop
    for swapped {
        // set swapped to false
        swapped = false
        // iterate through all of the elements in our list
        for i := 1; i < n; i++ {
            // if the current element is greater than the next
            // element, swap them
            if input[i-1] > input[i] {
                // log that we are swapping values for posterity
                //fmt.Println("Swapping")
                // swap values using Go's tuple assignment
                input[i], input[i-1] = input[i-1], input[i]
                // set swapped to true - this is important
                // if the loop ends and swapped is still equal
                // to false, our algorithm will assume the list is
                // fully sorted.
                swapped = true
            }
        }
    }
    // finally, print out the sorted list
    return input
}
