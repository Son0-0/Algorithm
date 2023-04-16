package main

import "fmt"

func twoOutOfThree(nums1 []int, nums2 []int, nums3 []int) []int {
	nums := make(map[int]int, 0)
	first, second, third := make(map[int]bool, 0), make(map[int]bool, 0), make(map[int]bool, 0)

	for _, num := range nums1 {
		nums[num]++
		first[num] = true
	}

	for _, num := range nums2 {
		nums[num]++
		second[num] = true
	}

	for _, num := range nums3 {
		nums[num]++
		third[num] = true
	}

	result := []int{}
	for key := range nums {
		if first[key] && second[key] {
			result = append(result, key)
		} else if second[key] && third[key] {
			result = append(result, key)
		} else if third[key] && first[key] {
			result = append(result, key)
		}
	}

	return result
}

func main() {
	fmt.Println(twoOutOfThree([]int{1, 1, 3, 2}, []int{2, 3}, []int{3}))
	fmt.Println(twoOutOfThree([]int{3, 1}, []int{2, 3}, []int{1, 2}))
	fmt.Println(twoOutOfThree([]int{1, 2, 2}, []int{4, 3, 3}, []int{5}))
}
