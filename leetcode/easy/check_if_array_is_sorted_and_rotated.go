package main

import (
	"fmt"
)

func check(nums []int) bool {
	result := 0
	length := len(nums)

	for i := 0; i < length; i++ {
		if nums[(i+1)%length] < nums[i] {
			result += 1
		}
	}

	return result <= 1
}

func main() {
	fmt.Println(check([]int{3, 4, 5, 1, 2}))
	fmt.Println(check([]int{2, 1, 3, 4}))
	fmt.Println(check([]int{1, 2, 3}))
}
