package main

import (
	"fmt"
	"strings"
)

func isPrefixOfWord(sentence string, searchWord string) int {
	target := strings.Split(sentence, " ")

	for idx, val := range target {
		if len(searchWord) <= len(string(val)) {
			if string(val[:len(searchWord)]) == searchWord {
				return idx + 1
			}
		}
	}

	return -1
}

func main() {
	fmt.Println(isPrefixOfWord("i love eating burger", "burg"))
	fmt.Println(isPrefixOfWord("this problem is an easy problem", "pro"))
	fmt.Println(isPrefixOfWord("i am tired", "you"))
}
