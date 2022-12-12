package main

import "fmt"

func longestPalindrome(s string) int {
	dict := make(map[string]int)

	for _, b := range s {
		s := string(b)

		if _, ok := dict[s]; ok {
			dict[s] += 1
		} else {
			dict[s] = 1
		}
	}

	result := 0
	odd := false
	for _, e := range dict {
		if e%2 == 0 {
			result += e
		} else {
			odd = true
			result += e - 1
		}
	}

	if odd {
		return result + 1
	} else {
		return result
	}
}

func main() {
	fmt.Println(longestPalindrome("abccccdd"))
	fmt.Println(longestPalindrome("a"))
	fmt.Println(longestPalindrome("yyyaakk"))
}
