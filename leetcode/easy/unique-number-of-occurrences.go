package main

import "fmt"

func uniqueOccurrences(arr []int) bool {
	nums := make(map[int]int)
	result := make(map[int]bool)

	for _, num := range arr {
		nums[num]++
	}

	for _, value := range nums {
		if _, e := result[value]; e {
			return false
		} else {
			result[value] = true
		}
	}

	return true
}

func main() {
	fmt.Println(uniqueOccurrences([]int{1, 2, 2, 1, 1, 3}))
	fmt.Println(uniqueOccurrences([]int{1, 2}))
	fmt.Println(uniqueOccurrences([]int{-3, 0, 1, -3, 1, 1, 1, -3, 10, 0}))
}
