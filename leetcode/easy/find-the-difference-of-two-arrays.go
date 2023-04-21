package main

import "fmt"

func findDifference(nums1 []int, nums2 []int) [][]int {
	result := make([][]int, 2)

	numsMap1 := make(map[int]bool)
	numsMap2 := make(map[int]bool)

	for _, num := range nums1 {
		numsMap1[num] = true
	}

	for _, num := range nums2 {
		numsMap2[num] = true
	}

	for key := range numsMap1 {
		if _, e := numsMap2[key]; !e {
			result[0] = append(result[0], key)
		}
	}

	for key := range numsMap2 {
		if _, e := numsMap1[key]; !e {
			result[1] = append(result[1], key)
		}
	}

	return result
}

func main() {
	fmt.Println(findDifference([]int{1, 2, 3}, []int{2, 4, 6}))
}
