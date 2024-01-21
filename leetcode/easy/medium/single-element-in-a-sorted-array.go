package main

import (
	"fmt"
)

func singleNonDuplicate(nums []int) int {
	if len(nums) == 1 {
		return nums[0]
	}

	result := 0
	length := len(nums) - 1
	var binarySearch func(int, int)
	var isValid func(int, int) bool

	isValid = func(index, target int) bool {
		if 0 < index && index < length {
			if nums[index-1] != target && nums[index+1] != target {
				return true
			}
		} else if index == 0 {
			if nums[index+1] != target {
				return true
			}
		} else if index == length {
			if nums[index-1] != target {
				return true
			}
		}

		return false
	}

	binarySearch = func(left, right int) {
		if right < left {
			return
		}

		mid := (left + right) / 2

		if isValid(mid, nums[mid]) {
			result = nums[mid]
			return
		}

		binarySearch(left, mid-1)
		binarySearch(mid+1, right)
	}

	binarySearch(0, length)

	return result
}

func main() {
	fmt.Println(singleNonDuplicate([]int{1}))
	fmt.Println(singleNonDuplicate([]int{1, 1, 2, 3, 3, 4, 4, 8, 8}))
	fmt.Println(singleNonDuplicate([]int{3, 3, 7, 7, 10, 11, 11}))
}
