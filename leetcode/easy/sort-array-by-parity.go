package main

import "fmt"

func sortArrayByParity(nums []int) []int {
	idx := 0

	for i, num := range nums {
		if num%2 == 0 {
			nums[idx], nums[i] = nums[i], nums[idx]
			idx++
		}
	}

	return nums
}

func main() {
	fmt.Println(sortArrayByParity([]int{3, 1, 2, 4}))
}
