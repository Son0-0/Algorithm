package main

import (
	"fmt"
	"strconv"
)

func summaryRanges(nums []int) []string {
	result := []string{}

	i := 0
	for i < len(nums) {
		temp := strconv.Itoa(nums[i])

		diff, end := 1, i
		for j := i + 1; j < len(nums); j++ {
			if nums[i]+diff == nums[j] {
				end = j
			} else {
				break
			}
			diff++
		}

		if end != i {
			temp += fmt.Sprintf("->%d", nums[end])
		}
		i = end + 1
		result = append(result, temp)
	}

	return result
}

// func summaryRanges(nums []int) []string {
// 	result := []string{}
// 	temp := ""

// 	if len(nums) == 0 {
// 		return []string{}
// 	} else if len(nums) == 1 {
// 		return []string{strconv.Itoa(nums[0])}
// 	}

// 	for i := 0; i < len(nums); i++ {
// 		if i == len(nums)-1 {
// 			if temp != "" {
// 				result = append(result, fmt.Sprintf("%s->%d", temp, nums[i]))
// 			} else {
// 				result = append(result, strconv.Itoa(nums[i]))
// 			}
// 			break
// 		}

// 		if nums[i] == nums[i+1]-1 {
// 			if temp == "" {
// 				temp += strconv.Itoa(nums[i])
// 			}
// 		} else {
// 			if temp != "" {
// 				result = append(result, fmt.Sprintf("%s->%d", temp, nums[i]))
// 				temp = ""
// 			} else {
// 				result = append(result, strconv.Itoa(nums[i]))
// 			}
// 		}
// 	}

// 	return result
// }

func main() {
	fmt.Println(summaryRanges([]int{}))
	fmt.Println(summaryRanges([]int{1}))
	fmt.Println(summaryRanges([]int{1, 2, 3, 4, 5, 6, 7}))
	fmt.Println(summaryRanges([]int{0, 1, 2, 4, 5, 7}))
	fmt.Println(summaryRanges([]int{0, 2, 3, 4, 6, 8, 9}))
}
