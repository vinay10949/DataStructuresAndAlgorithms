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

	fmt.Println("Insertion Sort Demo ")
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
	fmt.Println("Sorting it by insertion sort")
	fmt.Println("Final Sorted List ", insertionSort(lstIntegers))
}

func insertionSort(lstIntegers []int) []int {

	len := len(lstIntegers)
	for i := 1; i < len; i++ {
		for j := 0; j < i; j++ {
			if lstIntegers[j] > lstIntegers[i] {
				lstIntegers[j], lstIntegers[i] = lstIntegers[i], lstIntegers[j]
			}
		}
	}
	fmt.Println("LstIntegers ",lstIntegers)
	return lstIntegers

}
