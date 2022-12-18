package main

import (
	"fmt"
)

func minimumDeletions(nums []int) int {
	min, max := 100001, -100001
	minIndex, maxIndex := 0, 0

	for idx, num := range nums {
		if num < min {
			min = num
			minIndex = idx
		}

		if max < num {
			max = num
			maxIndex = idx
		}
	}

	if maxIndex < minIndex {
		minIndex, maxIndex = maxIndex, minIndex
	}

	// Case 1. left pop + right pop
	result := minIndex + 1 + len(nums) - maxIndex

	// Case 2. left pop
	if maxIndex+1 < result {
		result = maxIndex + 1
	}

	// Case 3. right pop
	if len(nums)-minIndex < result {
		result = len(nums) - minIndex
	}

	return result
}

func main() {
	fmt.Println(minimumDeletions([]int{2, 10, 7, 5, 4, 1, 8, 6}))
	fmt.Println(minimumDeletions([]int{0, -4, 19, 1, 8, -2, -3, 5}))
	fmt.Println(minimumDeletions([]int{101}))
}
