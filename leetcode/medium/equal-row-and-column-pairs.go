package main

import (
	"fmt"
	"strconv"
)

func equalPairs(grid [][]int) int {
	result := 0
	size := len(grid)
	pairs := make(map[string]int)

	for i := 0; i < size; i++ {
		temp := ""

		for j := 0; j < size; j++ {
			temp += strconv.Itoa(grid[i][j]) + "/"
		}

		pairs[temp]++
	}

	for i := 0; i < size; i++ {
		temp := ""

		for j := 0; j < size; j++ {
			temp += strconv.Itoa(grid[j][i]) + "/"
		}

		result += pairs[temp]
	}

	return result
}

func main() {
	fmt.Println(equalPairs([][]int{{3, 2, 1}, {1, 7, 6}, {2, 7, 7}}))
	fmt.Println(equalPairs([][]int{{3, 1, 2, 2}, {1, 4, 4, 5}, {2, 4, 2, 2}, {2, 4, 2, 2}}))
}
