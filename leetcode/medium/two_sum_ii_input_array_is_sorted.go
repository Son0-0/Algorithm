package main

import "fmt"

func twoSum(numbers []int, target int) []int {
	left, right := 0, len(numbers)-1

	for left < right {
		temp := numbers[left] + numbers[right]

		if temp == target {
			break
		} else if temp < target {
			left += 1
		} else {
			right -= 1
		}
	}

	return []int{left + 1, right + 1}
}

func main() {
	fmt.Println(twoSum([]int{2, 7, 11, 15}, 9))
	fmt.Println(twoSum([]int{2, 3, 4}, 6))
	fmt.Println(twoSum([]int{-1, 0}, -1))
}
