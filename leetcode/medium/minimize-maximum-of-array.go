package main

import (
	"fmt"
)

func max(nums []int) int {
	ret := -1

	for _, num := range nums {
		if ret < num {
			ret = num
		}
	}

	return ret
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func minimizeArrayValue(nums []int) int {
	left, right := 0, max(nums)
	result := max(nums)
	size := len(nums)

	var helper func(int) bool

	helper = func(target int) bool {
		if target < nums[0] {
			return false
		}

		canSub := 0
		for i := size - 1; i > 0; i-- {
			canSub = max([]int{nums[i] + canSub - target, 0})
		}

		return canSub+nums[0] <= target
	}

	for left < right {
		mid := (left + right) / 2

		if helper(mid) {
			right = mid
			result = min(result, mid)
		} else {
			left = mid + 1
		}
	}

	return result
}

func main() {
	fmt.Println(minimizeArrayValue([]int{3, 7, 1, 6}))
	fmt.Println(minimizeArrayValue([]int{10, 1}))
	fmt.Println(minimizeArrayValue([]int{13, 13, 20, 0, 8, 9, 9}))
	fmt.Println(minimizeArrayValue([]int{6, 9, 3, 8, 14}))
}
