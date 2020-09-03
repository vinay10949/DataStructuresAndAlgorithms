/*
Problem Statement:
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.



Note:



The solution set must not contain duplicate triplets.



Example:





Given array nums = [-1, 0, 1, 2, -1, -4],



A solution set is:

[

  [-1, 0, 1],

  [-1, -1, 2]

]


'''
*/

//s=Solution()
//print(s.threeSum( [-1, 0, 1, 2, -1, -4]))

package main

import (
	"fmt"
	"sort"
	"strconv"
)

var mapEle map[string]bool

func threeSum(arr []int) [][]int {
	elements := make([][]int, 0)
	sort.Ints(arr)

	for v, _ := range arr {
		l := v + 1
		r := len(arr) - 1
		for l < r {
			sum := arr[v] + arr[l] + arr[r]
			if sum == 0 {
				tmp := []int{arr[v], arr[l], arr[r]}
				sort.Ints(tmp)
				if _, ok := mapEle[strconv.Itoa(tmp[0])+""+strconv.Itoa(tmp[1])+""+strconv.Itoa(tmp[2])]; ok {
					l += 1
					r += 1
					continue
				}
				elements = append(elements, []int{arr[v], arr[l], arr[r]})
				l += 1
				r -= 1
				mapEle[strconv.Itoa(tmp[0])+""+strconv.Itoa(tmp[1])+""+strconv.Itoa(tmp[2])] = true
			} else {
				if sum <= 0 {
					l += 1
				} else {
					r -= 1
				}
			}
		}

	}

	return elements
}

func main() {
	arr := []int{-1, 0, 1, 2, -1, -4}
	mapEle = make(map[string]bool)
	fmt.Println(" Array given ", arr)
	output := threeSum(arr)
	fmt.Println(" Three Sum ", output)

}
