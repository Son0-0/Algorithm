package main

import "fmt"

func prefixesDivBy5(nums []int) []bool {
	result := make([]bool, len(nums))

	if nums[0] == 0 {
		result[0] = true
	}

	for i := 1; i < len(nums); i++ {
		nums[i] += nums[i-1] * 2 % 5
		if nums[i]%5 == 0 {
			result[i] = true
		}
	}

	return result
}

func main() {
	fmt.Println(prefixesDivBy5([]int{1, 0, 1}))
	fmt.Println(prefixesDivBy5([]int{0, 1, 1}))
	fmt.Println(prefixesDivBy5([]int{1, 1, 1}))
}
