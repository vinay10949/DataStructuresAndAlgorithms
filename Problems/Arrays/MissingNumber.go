package main

import (
	"fmt"
	"sort"
)

func main() {

	arr := []int{1, 3, 4, 5, 6}
	fmt.Println("Given Array ", arr)
	fmt.Println("Find missing element in an array using O(1) Space and O(n) time complexity")
	sort.Ints(arr)
	maxEle := arr[len(arr)-1]

	x := 0
	y := 0
	for _, i := range arr {
		x = x ^ i
	}

	for i := 1; i <= maxEle; i++ {
		y = y ^ i
	}
	fmt.Println(fmt.Sprintf("Missing Element in array is %d ", x^y))
}
