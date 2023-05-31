package main

import (
	"fmt"
	"strings"
)

func makeSmallestPalindrome(s string) string {
	size := len(s)
	result := make([]string, size)

	for i := 0; i < size/2; i++ {
		if s[i] < s[size-i-1] {
			result[i] = string(s[i])
			result[size-i-1] = string(s[i])
		} else {
			result[i] = string(s[size-i-1])
			result[size-i-1] = string(s[size-i-1])
		}
	}

	if size%2 != 0 {
		result[size/2] = string(s[size/2])
	}

	return strings.Join(result, "")
}

func main() {
	fmt.Println(makeSmallestPalindrome("egcfe"))
	fmt.Println(makeSmallestPalindrome("abcd"))
	fmt.Println(makeSmallestPalindrome("seven"))
}
