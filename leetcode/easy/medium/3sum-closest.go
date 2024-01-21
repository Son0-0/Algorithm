package main

import (
	"fmt"
	"sort"
)

func abs(target int) int {
	if target < 0 {
		return -1 * target
	}
	return target
}

func threeSumClosest(nums []int, target int) int {
	result := []int{100000, 0}
	n := len(nums) - 1
	sort.Ints(nums)

	for i := 0; i < len(nums); i++ {
		left, right := i+1, n

		for left < right {
			curSum := nums[i] + nums[left] + nums[right]
			temp := abs(target - curSum)

			if temp < result[0] {
				result[0] = temp
				result[1] = curSum
			}

			if curSum < target {
				left++
			} else if target < curSum {
				right--
			} else {
				return curSum
			}
		}

	}

	return result[1]
}

func main() {
	fmt.Println(threeSumClosest([]int{-1, 2, 1, -4}, 1))
	fmt.Println(threeSumClosest([]int{0, 0, 0}, 1))
}
