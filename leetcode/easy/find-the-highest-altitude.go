package main

import "fmt"

func max(a, b int) int {
	if a < b {
		return b
	}
	return a
}

func largestAltitude(gain []int) int {
	result, start := 0, 0

	for _, g := range gain {
		start += g
		result = max(result, start)
	}

	return result
}

func main() {
	fmt.Println(largestAltitude([]int{-5, 1, 5, 0, -7}))
	fmt.Println(largestAltitude([]int{-4, -3, -2, -1, 4, 3, 2}))
}
