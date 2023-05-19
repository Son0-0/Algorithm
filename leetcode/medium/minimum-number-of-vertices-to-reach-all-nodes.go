package main

import (
	"fmt"
)

func findSmallestSetOfVertices(n int, edges [][]int) []int {
	result := make([]int, 0)
	indegrees := make([]int, n)

	for _, edge := range edges {
		indegrees[edge[1]]++
	}

	for idx, v := range indegrees {
		if v == 0 {
			result = append(result, idx)
		}
	}

	return result
}

func main() {
	fmt.Println(findSmallestSetOfVertices(6, [][]int{{0, 1}, {0, 2}, {2, 5}, {3, 4}, {4, 2}}))
}
