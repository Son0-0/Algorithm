package main

import (
	"fmt"
	"strings"
)

func maxRepeating(sequence string, word string) int {
	target := word
	result := 0

	for i := 1; i <= len(sequence)/len(word); i++ {
		if strings.Contains(sequence, target) {
			result = i
			target += word
		} else {
			break
		}
	}

	return result
}

func main() {
	fmt.Println(maxRepeating("ababc", "ab"))
	fmt.Println(maxRepeating("ababc", "ba"))
	fmt.Println(maxRepeating("ababc", "ac"))
}
