package main

import (
	"fmt"
	"strconv"
)

func hammingDistance(x int, y int) int {
	result := 0

	for _, c := range strconv.FormatInt(int64(x^y), 2) {
		if c == '1' {
			result++
		}
	}

	return result
}

// Leetcode Solution
// func hammingDistance(x int, y int) int {
//     var dist int
//     for v := x^y; v > 0; dist++ {
//         v = v & (v-1)
//     }
//     return dist
// }

func main() {
	fmt.Println(hammingDistance(1, 4))
	fmt.Println(hammingDistance(3, 1))
}
