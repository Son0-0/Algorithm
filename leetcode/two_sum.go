package main

import (
	"fmt"
)

func twoSum(nums []int, target int) []int {

	_map := make(map[int]int)

	for idx, element := range nums {
		if index, exists := _map[target-element]; exists {
			return []int{index, idx}
		}
		_map[element] = idx
	}

	return []int{0, 0}
}

func main() {
	fmt.Println(twoSum([]int{3, 2, 4}, 6))
	fmt.Println(twoSum([]int{2, 7, 11, 15}, 9))
}
