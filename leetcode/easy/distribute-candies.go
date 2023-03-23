package main

import "fmt"

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func distributeCandies(candyType []int) int {
	advice := len(candyType) / 2

	cType := make(map[int]int)

	for _, candy := range candyType {
		cType[candy]++
	}

	return min(advice, len(cType))
}

func main() {
	fmt.Println(distributeCandies([]int{1, 1, 2, 2, 3, 3}))
	fmt.Println(distributeCandies([]int{1, 1, 2, 3}))
	fmt.Println(distributeCandies([]int{6, 6, 6, 6}))
}
