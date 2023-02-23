package main

import "fmt"

func intersection(nums1 []int, nums2 []int) []int {
	nums := make(map[int]bool)
	result := []int{}

	for _, num := range nums1 {
		nums[num] = true
	}

	for _, num := range nums2 {
		if tf, e := nums[num]; e && tf {
			result = append(result, num)
			nums[num] = false
		}
	}

	return result
}

func main() {
	fmt.Println(intersection([]int{1, 2, 2, 1}, []int{2, 2}))
	fmt.Println(intersection([]int{4, 9, 5}, []int{9, 4, 9, 8, 4}))
}
