package main

import (
	"fmt"
)

func findLengthOfLCIS(nums []int) int {
	result := 1
	length := 1
	prev := nums[0]

	for i := 1; i < len(nums); i++ {
		if prev < nums[i] {
			prev = nums[i]
			length += 1
		} else {
			length = 1
			prev = nums[i]
		}

		if result < length {
			result = length
		}
	}

	return result
}

func main() {
	fmt.Println(findLengthOfLCIS([]int{1, 3, 5, 4, 7}))
	fmt.Println(findLengthOfLCIS([]int{2, 2, 2, 2, 2}))
	fmt.Println(findLengthOfLCIS([]int{1, 3, 5, 4, 2, 3, 4, 5}))
}
