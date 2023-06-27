package main

import "fmt"

func abs(target int) int {
	if target < 0 {
		return -target
	}
	return target
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func shortestToChar(s string, c byte) []int {
	result := make([]int, len(s))

	pos := -1
	for i := 0; i < len(s); i++ {
		if s[i] == c {
			pos = i
		} else {
			if pos != -1 {
				result[i] = abs(i - pos)
			}
		}
	}

	pos = -1
	for i := len(s) - 1; i >= 0; i-- {
		if s[i] == c {
			pos = i
		} else {
			if pos != -1 {
				target := abs(i - pos)
				if result[i] != 0 {
					result[i] = min(result[i], target)
				} else {
					result[i] = target
				}
			}
		}
	}

	return result
}

func main() {
	fmt.Println(shortestToChar("loveleetcode", 'e'))
	fmt.Println(shortestToChar("aaab", 'b'))
}
