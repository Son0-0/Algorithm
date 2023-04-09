package main

import "fmt"

func max(a, b int) int {
	if a < b {
		return b
	}
	return a
}

func sumDigit(target int) int {
	sum := 0

	for target > 0 {
		sum += target % 10
		target /= 10
	}

	return sum
}

func countLargestGroup(n int) int {
	result := 0
	numMap := make(map[int][]int)
	size := 0

	for i := 1; i <= n; i++ {
		numMap[sumDigit(i)] = append(numMap[sumDigit(i)], i)
	}

	for key := range numMap {
		size = max(size, len(numMap[key]))
	}

	for key := range numMap {
		if len(numMap[key]) == size {
			result++
		}
	}

	return result
}

func main() {
	fmt.Println(countLargestGroup(13))
	fmt.Println(countLargestGroup(2))
}
