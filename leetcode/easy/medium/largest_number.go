package main

import (
	"fmt"
	"sort"
	"strconv"
)

func largestNumber(nums []int) string {
	strs := []string{}
	for _, num := range nums {
		strs = append(strs, strconv.Itoa(num))
	}

	sort.Slice(strs, func(a, b int) bool {
		return strs[a]+strs[b] > strs[b]+strs[a]
	})

	result := ""
	if strs[0] == "0" {
		return "0"
	}

	for _, str := range strs {
		result += str
	}

	return result
}

func main() {
	fmt.Println(largestNumber([]int{10, 2}))
	fmt.Println(largestNumber([]int{3, 30, 34, 5, 9}))
}
