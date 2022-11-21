package main

import (
	"fmt"
	"sort"
)

func removeElement(nums []int, val int) int {
	result := len(nums)

	for idx, e := range nums {
		if e == val {
			nums[idx] = 101
			result -= 1
		}
	}

	sort.Ints(nums)

	return result
}

func main() {
	fmt.Println(removeElement([]int{3, 2, 2, 3}, 3))
	fmt.Println(removeElement([]int{0, 1, 2, 2, 3, 0, 4, 2}, 2))
}
