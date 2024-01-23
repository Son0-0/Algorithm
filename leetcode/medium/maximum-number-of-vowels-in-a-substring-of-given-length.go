package main

import "fmt"

func check(c byte) bool {
	return c == 'a' || c =='e' || c == 'i' || c == 'o' || c == 'u'
}

func maxVowels(s string, k int) int {
	cur := 0

	for i := 0; i < k; i++ {
		target := s[i]

		if check(target) {
			cur++
		}
	}

	result := cur

	for i := k; i < len(s); i++ {
		if check(s[i]) {
			cur++
		}

		if check(s[i-k]) {
			cur--
		}

		if result < cur {
			result = cur
		}
	}

	return result
}

func main() {
	fmt.Println(maxVowels("abciiidef", 3))
	fmt.Println(maxVowels("aeiou", 2))
	fmt.Println(maxVowels("leetcode", 3))
}