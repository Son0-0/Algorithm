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

func intToByteString(target int) string {
	result := ""

	for target > 0 {
		result = strconv.Itoa(target%2) + result
		target /= 2
	}

	return result
}

func binaryGap(n int) int {
	result := 0

	prev := -1
	for i, c := range intToByteString(n) {
		if prev != -1 {
			if c == '1' {
				result = max(result, i-prev)
				prev = i
			}
		} else {
			if c == '1' {
				prev = i
			}
		}
	}

	return result
}

func main() {
	fmt.Println(binaryGap(22))
	fmt.Println(binaryGap(8))
	fmt.Println(binaryGap(5))
}
