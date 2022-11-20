package main

import (
	"fmt"
	"sort"
)

func removeDuplicates(nums []int) int {
	result := len(nums)

	for idx, e := range nums {
		for i := 0; i < idx; i++ {
			if nums[i] == e {
				nums[idx] = 101
				result -= 1
				break
			}
		}
	}

	sort.Ints(nums)

	return result
}

func main() {
	fmt.Println(removeDuplicates([]int{0, 0, 1, 1, 1, 2, 2, 3, 3, 4}))
	fmt.Println(removeDuplicates([]int{1, 1, 2}))
}
