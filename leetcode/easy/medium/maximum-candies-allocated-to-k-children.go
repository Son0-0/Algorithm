package main

import "fmt"

func max(nums []int) int {
	result := -1

	for _, num := range nums {
		if result < num {
			result = num
		}
	}

	return result
}

func sum(nums []int) int64 {
	result := int64(0)

	for _, num := range nums {
		result += int64(num)
	}

	return result
}

func maximumCandies(candies []int, k int64) int {
	left, right := 0, max(candies)

	if sum(candies) < k {
		return 0
	}

	for left < right {
		mid := (left + right + 1) / 2

		temp := int64(0)

		for _, candy := range candies {
			temp += int64(candy / mid)
		}

		if temp < k {
			right = mid - 1
		} else {
			left = mid
		}
	}

	return left
}

func main() {
	fmt.Println(maximumCandies([]int{5, 8, 6}, 3))
}
