package main

import (
	"fmt"
	"sort"
)

func arrayRankTransform(arr []int) []int {
	result := []int{}
	rank := make(map[int]int)

	tempArray := make([]int, len(arr))
	copy(tempArray, arr)

	sort.Ints(tempArray)

	prev := 0
	cur := 1

	for _, num := range tempArray {
		if num != prev {
			rank[num] = cur
			cur += 1
			prev = num
		}
	}

	for _, num := range arr {
		result = append(result, rank[num])
	}

	return result
}

func main() {
	fmt.Println(arrayRankTransform([]int{40, 10, 20, 30}))
	fmt.Println(arrayRankTransform([]int{100, 100, 100}))
	fmt.Println(arrayRankTransform([]int{37, 12, 28, 9, 100, 56, 80, 5, 12}))
}
