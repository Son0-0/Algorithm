package main

import (
	"fmt"
	"sort"
)

func minNumber(nums1 []int, nums2 []int) int {
	sort.Ints(nums1)
	sort.Ints(nums2)

	for _, i := range nums1 {
		for _, j := range nums2 {
			if i == j {
				return i
			}
		}
	}

	a, b := nums1[0], nums2[0]

	if a < b {
		return a*10 + b
	}
	return b*10 + a
}

func main() {
	fmt.Println(minNumber([]int{4, 1, 3}, []int{5, 7}))
	fmt.Println(minNumber([]int{3, 5, 2, 6}, []int{3, 1, 7}))
}
