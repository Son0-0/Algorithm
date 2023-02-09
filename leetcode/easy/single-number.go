package main

import "fmt"

func singleNumber(nums []int) int {
	numMap := make(map[int]int)

	for _, num := range nums {
		numMap[num]++
	}

	for key := range numMap {
		if numMap[key] == 1 {
			return key
		}
	}

	return 0
}

func main() {
	fmt.Println(singleNumber([]int{2, 2, 1}))
	fmt.Println(singleNumber([]int{4, 1, 2, 1, 2}))
	fmt.Println(singleNumber([]int{1}))
}
