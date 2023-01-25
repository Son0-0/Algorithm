package main

import (
	"fmt"
)

func largeGroupPositions(s string) [][]int {
	result := [][]int{}

	i := 0

	for i < len(s) {
		length, right := 1, i
		for j := i + 1; j < len(s); j++ {
			if s[i] == s[j] {
				length++
			} else {
				break
			}
			right++
		}

		if 3 <= length {
			result = append(result, []int{i, right})
		}

		i = right + 1
	}

	// sort.SliceStable(result, func(i, j int) bool {
	// 	if result[i][0] < result[j][0] {
	// 		return true
	// 	}
	// 	return false
	// })

	return result
}

func main() {
	fmt.Println(largeGroupPositions("abbxxxxzzy"))
	fmt.Println(largeGroupPositions("abc"))
	fmt.Println(largeGroupPositions("abcdddeeeeaabbbcd"))
}
