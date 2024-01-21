package main

import (
	"fmt"
)

func min(a int, b int) int {
	if a < b {
		return a
	}
	return b
}

func max(a int, b int) int {
	if a < b {
		return b
	}
	return a
}

func maxArea(height []int) int {
	result := 0
	left, right := 0, len(height)-1

	for left < right {
		w := right - left
		h := min(height[left], height[right])

		result = max(result, w*h)

		if left == right {
			left += 1
			right -= 1
		} else if h == height[left] {
			left += 1
		} else if h == height[right] {
			right -= 1
		}
	}

	return result
}

func main() {
	fmt.Println(maxArea([]int{1, 8, 6, 2, 5, 4, 8, 3, 7}))
	fmt.Println(maxArea([]int{1, 1}))
}
