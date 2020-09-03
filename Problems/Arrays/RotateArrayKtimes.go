package main

import "fmt"

//Time Complexity O(n*k)
func rotateArrayOnce(arr []int) []int {
	var slice = make([]int, len(arr))
	slice[0] = arr[len(arr)-1]
	i := 1
	for _, ele := range arr[0 : len(arr)-1] {
		slice[i] = ele
		i = i + 1
	}
	return slice
}

func reverse(arr []int, a int, b int) []int {
	for a <= b {
		temp := arr[a]
		arr[a] = arr[b]
		arr[b] = temp
		a += 1
		b -= 1
	}
	return arr
}

//Time Complexity O(n) Space Complexity O(1)
func rotateKtimes(arr []int, n int, k int) []int {
	arr = reverse(arr, n-k, n-1)
	arr = reverse(arr, 0, n-k-1)
	arr = reverse(arr, 0, n-1)
	return arr
}

var k int

func main() {
	fmt.Print("Enter no of times array needs to be rotated : ")
	fmt.Scanf("%d", &k)
	tempK := k
	fmt.Println(fmt.Sprintf("Rotating array %d Times ", k))
	arr := []int{1, 2, 3, 4, 5, 6, 7}
	fmt.Println("Original Array ", arr)
	i := 0
	var l []int
	//Time Complexity O(n*k)
	for k > 0 {
		fmt.Println(fmt.Sprintf("Rotating Array %d time", i))
		if i == 0 {
			l = rotateArrayOnce(arr)
		} else {
			l = rotateArrayOnce(l)
		}
		i = i + 1
		k = k - 1
	}
	fmt.Println(fmt.Sprintf("After Rotation Array %d Time : %v", i, l))

	fmt.Println(rotateKtimes(arr, len(arr), tempK))
}
