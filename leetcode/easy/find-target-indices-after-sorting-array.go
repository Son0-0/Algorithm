package main

import (
	"fmt"
	"sort"
)

func targetIndices(nums []int, target int) []int {
	result := make([]int, 0)
	sort.Ints(nums)

	for idx, num := range nums {
		if num == target {
			result = append(result, idx)
		}
	}

	return result
}

func main() {
	fmt.Println(targetIndices([]int{1, 2, 5, 2, 3}, 2))
	fmt.Println(targetIndices([]int{1, 2, 5, 2, 3}, 3))
	fmt.Println(targetIndices([]int{1, 2, 5, 2, 3}, 5))
}
