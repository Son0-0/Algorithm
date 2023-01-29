package main

import (
	"fmt"
	"strconv"
)

func max(a, b int) int {
	if a < b {
		return b
	}
	return a
}

func convert(target int) int {
	temp := strconv.Itoa(target)
	result := 0

	for _, c := range temp {
		t, _ := strconv.Atoi(string(c))
		result += t
	}

	return result
}

func countBalls(lowLimit int, highLimit int) int {
	result := 0
	box := make(map[int]int)

	for i := lowLimit; i <= highLimit; i++ {
		target := convert(i)
		box[target]++
		result = max(result, box[target])
	}

	return result
}

func main() {
	fmt.Println(countBalls(1, 10))
	fmt.Println(countBalls(5, 15))
	fmt.Println(countBalls(19, 28))
}
