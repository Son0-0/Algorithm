package main

import "fmt"

func searchRange(nums []int, target int) []int {
	left, right := 0, len(nums)-1
	first := -1

	// search for first element
	for left <= right {
		mid := left + (right-left)/2

		if nums[mid] == target {
			first = mid
		}

		if target <= nums[mid] {
			right = mid - 1
		} else {
			left = mid + 1
		}
	}

	left, right = 0, len(nums)-1
	last := -1

	// search for last element
	for left <= right {
		mid := left + (right-left)/2

		if nums[mid] == target {
			last = mid
		}

		if nums[mid] <= target {
			left = mid + 1
		} else {
			right = mid - 1
		}
	}

	return []int{first, last}
}

func main() {
	fmt.Println(searchRange([]int{5, 7, 7, 8, 8, 10}, 8))
	fmt.Println(searchRange([]int{5, 7, 7, 8, 8, 10}, 6))
	fmt.Println(searchRange([]int{}, 0))
}
