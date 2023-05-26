package main

import (
	"fmt"
)

func smallerNumbersThanCurrent(nums []int) []int {
	numMap := make(map[int]int, 0)
	maxValue := 0

	for _, num := range nums {
		numMap[num]++
		if maxValue < num {
			maxValue = num
		}
	}

	for i := 1; i <= maxValue; i++ {
		numMap[i] += numMap[i-1]
	}

	result := make([]int, 0)

	for _, num := range nums {
		result = append(result, numMap[num-1])
	}

	return result
}

func main() {
	fmt.Println(smallerNumbersThanCurrent([]int{8, 1, 2, 2, 3}))
	fmt.Println(smallerNumbersThanCurrent([]int{6, 5, 4, 8}))
	fmt.Println(smallerNumbersThanCurrent([]int{7, 7, 7, 7}))
}
