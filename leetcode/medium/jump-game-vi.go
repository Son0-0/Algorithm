package main

import (
	"fmt"
)

func maxResult(nums []int, k int) int {
	q := make([]int, 0)
	q = append(q, 0)

	for i := 1; i < len(nums); i++ {
		for len(q) > 0 && i-k > q[0] {
			q = q[1:]
		}

		nums[i] += nums[q[0]]

		for len(q) > 0 && nums[q[len(q)-1]] < nums[i] {
			q = q[:len(q)-1]
		}

		q = append(q, i)
	}

	return nums[len(nums)-1]
}

func main() {
	fmt.Println(maxResult([]int{1}, 1))
	fmt.Println(maxResult([]int{1, -1, -2, 4, -7, 3}, 2))
	fmt.Println(maxResult([]int{10, -5, -2, 4, 0, 3}, 3))
	fmt.Println(maxResult([]int{1, -5, -20, 4, -1, 3, -6, -3}, 2))
}

// TLE
// func max(a, b int) int {
// 	if a < b {
// 		return b
// 	}
// 	return a
// }

// func maxResult(nums []int, k int) int {
// 	dp := []int{nums[0]}

// 	for i := 1; i < len(nums); i++ {
// 		temp := int(math.Inf(-1))
// 		for j := 1; j <= k; j++ {
// 			if i-j < 0 {
// 				break
// 			}

// 			temp = max(temp, dp[i-j]+nums[i])
// 		}

// 		dp = append(dp, temp)
// 	}

// 	return dp[len(dp)-1]
// }
