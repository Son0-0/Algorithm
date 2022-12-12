package main

import (
	"sort"
)

func merge(nums1 []int, m int, nums2 []int, n int) {
	temp := []int{}

	for i := 0; i < m; i++ {
		temp = append(temp, nums1[i])
	}

	for i := 0; i < n; i++ {
		temp = append(temp, nums2[i])
	}

	sort.Ints(temp)

	for i := 0; i < m+n-len(temp); i++ {
		temp = append(temp, 0)
	}

	copy(nums1, temp)
}

func main() {
	merge([]int{1, 2, 3, 0, 0, 0}, 3, []int{2, 5, 6}, 3)
	merge([]int{1}, 1, []int{}, 0)
	merge([]int{0}, 0, []int{1}, 1)
}
