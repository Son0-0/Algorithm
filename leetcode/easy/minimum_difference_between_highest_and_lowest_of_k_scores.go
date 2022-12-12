package main

import (
	"fmt"
	"sort"
)

func minimumDifference(nums []int, k int) int {
	if k == 1 {
		return 0
	}

	sort.Ints(nums)

	min := 100001
	for i := 0; i <= len(nums)-k; i++ {
		target := nums[i+k-1] - nums[i]
		if target < min {
			min = target
		}
	}

	return min
}

func main() {
	fmt.Println(minimumDifference([]int{90}, 1))
	fmt.Println(minimumDifference([]int{9, 4, 1, 7}, 2))
}
