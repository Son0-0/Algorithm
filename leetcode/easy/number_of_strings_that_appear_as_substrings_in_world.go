package main

import (
	"fmt"
	"strings"
)

func numOfStrings(patterns []string, word string) int {
	result := 0
	for _, pattern := range patterns {
		if strings.Contains(word, pattern) {
			result += 1
		}
	}

	return result
}

func main() {
	fmt.Println(numOfStrings([]string{"a", "abc", "bc", "d"}, "abc"))
	fmt.Println(numOfStrings([]string{"a", "b", "c"}, "aaaaabbbbb"))
}
