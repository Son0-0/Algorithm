package main

import "strconv"

func isValid(target int) bool {
	for _, c := range strconv.Itoa(target) {
		if c == '0' {
			return false
		}
	}
	return true
}

func getNoZeroIntegers(n int) []int {
	result := make([]int, 2)

	for i := 1; i < n; i++ {
		if isValid(i) && isValid(n-i) {
			result[0], result[1] = i, n-i
			break
		}
	}

	return result
}
