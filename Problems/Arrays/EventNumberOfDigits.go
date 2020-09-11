package main

import "fmt"
import "math"

func calculateEvent(nos [5]int) int {
	num_even := 0

	for _, i := range nos {

		noOfDigits := math.Floor(math.Log10(float64(i))) + 1
		if  math.Mod(noOfDigits,2) == 0 {
			num_even++
		}

	}

	return num_even

}
func main() {

	arr := [5]int{1, 23, 2445, 333, 2341}
	fmt.Println("Array ", arr)
	fmt.Println("No of Even digit nos : ", calculateEvent(arr))

}
