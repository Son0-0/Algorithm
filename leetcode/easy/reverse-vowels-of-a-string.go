package main

import (
	"fmt"
)

func isVowel(r rune) bool {
	return (r == 'a' || r == 'e' || r == 'i' || r == 'o' || r == 'u') || (r == 'A' || r == 'E' || r == 'I' || r == 'O' || r == 'U')
}

func reverseVowels(s string) string {
	result := make([]rune, len(s))
	left, right := 0, len(s)-1

	for i, r := range s {
		result[i] = r
	}

	for left < right {
		if !isVowel(rune(s[right])) {
			right--
			continue
		}

		if !isVowel(rune(s[left])) {
			left++
			continue
		}

		result[left], result[right] = result[right], result[left]
		left++
		right--
	}

	return string(result)
}

func main() {
	fmt.Println(reverseVowels("hello"))
	fmt.Println(reverseVowels("leetcode"))
}
