package main

import "fmt"

func isAnagram(s string, t string) bool {
	alpha := make([]int, 26)

	if len(t) != len(s) {
		return false
	}

	for i := 0; i < len(s); i++ {
		alpha[s[i]-97] += 1
		alpha[t[i]-97] -= 1
	}

	for i := 0; i < 26; i++ {
		if alpha[i] != 0 {
			return false
		}
	}

	return true
}

func main() {
	fmt.Println(isAnagram("anagram", "nagaram"))
	fmt.Println(isAnagram("rat", "car"))
}
