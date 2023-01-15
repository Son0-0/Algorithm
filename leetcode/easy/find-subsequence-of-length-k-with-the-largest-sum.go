package main

import (
	"fmt"
	"sort"
)

func maxSubsequence(nums []int, k int) []int {
	result, target := []int{}, make([]int, len(nums))
	copy(target, nums)
	sort.Slice(target, func(i, j int) bool {
		return target[i] > target[j]
	})

	targetDict := make(map[int]int)
	for _, num := range target[:k] {
		targetDict[num] += 1
	}

	for _, num := range nums {
		if targetDict[num] > 0 {
			targetDict[num] -= 1
			result = append(result, num)
		}
	}

	return result
}

func main() {
	fmt.Println(maxSubsequence([]int{2, 1, 3, 3}, 2))
	fmt.Println(maxSubsequence([]int{-1, -2, 3, 4}, 3))
	fmt.Println(maxSubsequence([]int{3, 4, 3, 3}, 2))
	fmt.Println(maxSubsequence([]int{-8, -94, -30, -98, -27, 62, 26}, 7))
}
