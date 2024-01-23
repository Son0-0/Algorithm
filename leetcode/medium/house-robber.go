package main

import "fmt"

func max(a, b int) int {
	if a < b {
		return b
	}
	return a
}

func rob(nums []int) int {
	size := len(nums)

	if size == 0 {
		return 0
	} else if size == 1 {
		return nums[0]
	} else if size == 2 {
		return max(nums[0], nums[1])
	}

	result := 0
	dp := make([]int, size)

	dp[0] = nums[0]
	dp[1] = nums[1]
	dp[2] = nums[0] + nums[2]

	for idx := 0; idx < size; idx++ {
		if 2 < idx {
			dp[idx] = nums[idx] + max(dp[idx-2], dp[idx-3])
		}
		result = max(result, dp[idx])
	}

	return result
}

func main() {
	nums := []int{2, 7, 9, 3, 1}
	fmt.Println(rob(nums))
}
