package main

import (
	"fmt"
	"sort"
)

// User Solution
// func findDisappearedNumbers(nums []int) []int {
// 	result := []int{}

// 	for _, e := range nums {
// 		target := int(math.Abs(float64(e))) - 1
// 		if 0 < nums[target] {
// 			nums[target] *= -1
// 		}
// 	}

// 	for idx, e := range nums {
// 		if 0 < e {
// 			result = append(result, idx+1)
// 		}
// 	}

// 	return result
// }

// * My Solution
func findDisappearedNumbers(nums []int) []int {
	result := []int{}

	for i := 1; i <= len(nums); i++ {
		result = append(result, i)
	}

	for _, e := range nums {
		result[e-1] = 0
	}

	sort.Ints(result)

	for 0 < len(result) && result[0] == 0 {
		result = result[1:]
	}

	return result
}

func main() {
	fmt.Println(findDisappearedNumbers([]int{4, 3, 2, 7, 8, 2, 3, 1}))
	fmt.Println(findDisappearedNumbers([]int{1, 1}))
}
