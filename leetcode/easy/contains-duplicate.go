package main

import "fmt"

func containsDuplicate(nums []int) bool {
	dup := make(map[int]bool)

	for _, num := range nums {
		if _, e := dup[num]; e {
			return true
		} else {
			dup[num] = true
		}
	}

	return false
}

func main() {
	fmt.Println(containsDuplicate([]int{1, 2, 3, 1}))
}
