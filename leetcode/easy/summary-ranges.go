package main

import (
	"fmt"
	"strconv"
)

func summaryRanges(nums []int) []string {
	if len(nums) == 0 {
		return []string{}
	}

	result := make([]string, 0)

	cur := nums[0]
	con := false

	for i := 1; i < len(nums); i++ {
		if nums[i] == nums[i-1]+1 {
			con = true
		} else {
			if con == true {
				result = append(result, strconv.Itoa(cur)+"->"+strconv.Itoa(nums[i-1]))
			} else {
				result = append(result, strconv.Itoa(cur))
			}
			cur = nums[i]
			con = false
		}
	}

	if con {
		result = append(result, strconv.Itoa(cur)+"->"+strconv.Itoa(nums[len(nums)-1]))
	} else {
		result = append(result, strconv.Itoa(cur))
	}

	return result
}

func main() {
	fmt.Println(summaryRanges([]int{0, 1, 2, 4, 5, 7}))
	fmt.Println(summaryRanges([]int{0, 2, 3, 4, 6, 8, 9}))
	fmt.Println(summaryRanges([]int{-3, -2}))
}
