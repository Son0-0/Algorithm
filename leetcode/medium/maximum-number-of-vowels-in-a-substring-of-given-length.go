package main

import "fmt"

func maxVowels(s string, k int) int {
    result := 0

	cur, pos := 0, k-1

	for i := 0; i < k; i++ {
		target := s[i]

		if target == 'a' || target =='e' || target == 'i' || target == 'o' || target == 'u' {
			cur++
		}
	}

	fmt.Println(cur, pos)

	return result
}

func main() {
	fmt.Println(maxVowels("abciiidef", 3))
	fmt.Println(maxVowels("aeiou", 2))
	fmt.Println(maxVowels("leetcode", 3))
}