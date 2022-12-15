package main

import (
	"fmt"
)

func findSubsequences(nums []int) [][]int {
	length := len(nums)
	result := [][]int{}

	var dfs func(int, int, []int)

	dfs = func(cur int, prev int, visited []int) {
		if 1 < len(visited) {
			temp := make([]int, len(visited))
			copy(temp, visited)

			result = append(result, temp)
		}

		dup := make(map[int]bool)

		for i := cur; i < length; i++ {
			if prev <= nums[i] && !dup[nums[i]] {
				dup[nums[i]] = true
				dfs(i+1, nums[i], append(visited, nums[i]))
			}
		}
	}

	dfs(0, -101, []int{})

	return result
}

func main() {
	fmt.Println(findSubsequences([]int{4, 6, 7, 7}))
	fmt.Println(findSubsequences([]int{4, 4, 3, 2, 1}))
}
