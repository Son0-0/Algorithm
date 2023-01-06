package main

import (
	"fmt"
)

func max(a, b int) int {
	if a < b {
		return b
	}
	return a
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func intervalIntersection(firstList [][]int, secondList [][]int) [][]int {
	result := [][]int{}

	i, j := 0, 0

	for i < len(firstList) && j < len(secondList) {
		aL, aR := firstList[i][0], firstList[i][1]
		bL, bR := secondList[j][0], secondList[j][1]

		if aL <= bR && bL <= aR {
			result = append(result, []int{max(aL, bL), min(aR, bR)})
		}

		if aR <= bR {
			i += 1
		} else {
			j += 1
		}
	}

	return result
}

func main() {
	fmt.Println(intervalIntersection([][]int{{0, 2}, {5, 10}, {13, 23}, {24, 25}}, [][]int{{1, 5}, {8, 12}, {15, 24}, {25, 26}}))
	fmt.Println(intervalIntersection([][]int{{1, 3}, {5, 9}}, [][]int{}))
}
