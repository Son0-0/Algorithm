package main

import "fmt"

func max(a, b int) int {
	if a < b {
		return b
	}
	return a
}

func maxScore(s string) int {
	result := 0
	cnt := 0

	for _, c := range s {
		if c == '1' {
			cnt++
		}
	}

	left := 0
	for i := 0; i < len(s)-1; i++ {
		if s[i] == '1' {
			cnt--
		} else {
			left++
		}
		result = max(result, cnt+left)
	}

	return result
}

func main() {
	fmt.Println(maxScore("011101"))
	fmt.Println(maxScore("00111"))
	fmt.Println(maxScore("1111"))
	fmt.Println(maxScore("00"))
}
