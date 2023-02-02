package main

import "fmt"

func max(a, b int) int {
	if a < b {
		return b
	}
	return a
}

func largestAltitude(gain []int) int {
	result, cur := 0, 0

	for _, num := range gain {
		cur += num
		result = max(result, cur)
	}

	return result
}

func main() {
	fmt.Println(largestAltitude([]int{-5, 1, 5, 0, -7}))
	fmt.Println(largestAltitude([]int{-4, -3, -2, -1, 4, 3, 2}))
}
