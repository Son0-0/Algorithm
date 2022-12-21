package main

import "fmt"

func productExceptSelf(nums []int) []int {
	prefix, suffix := make([]int, len(nums)), make([]int, len(nums))

	for i := 0; i < len(nums); i++ {
		prefix[i], suffix[i] = 1, 1
	}

	for i := 1; i < len(nums); i++ {
		prefix[i] = prefix[i-1] * nums[i-1]
		suffix[len(nums)-1-i] = suffix[len(nums)-i] * nums[len(nums)-i]
	}

	result := make([]int, len(nums))
	for i := 0; i < len(nums); i++ {
		result[i] = prefix[i] * suffix[i]
	}

	return result
}

func main() {
	fmt.Println(productExceptSelf([]int{1, 2, 3, 4}))
	fmt.Println(productExceptSelf([]int{-1, 1, 0, -3, 3}))
}
