package main

import (
	"fmt"
	"strconv"
)

func isPalindrom(target string) bool {
	for i := 0; i < len(target)/2; i++ {
		if target[i] != target[len(target)-i-1] {
			return false
		}
	}
	return true
}

func baseConvert(base, target int) string {
	result := ""

	for base <= target {
		result = strconv.Itoa(target%base) + result
		target /= base
	}

	return strconv.Itoa(target) + result
}

func isStrictlyPalindromic(n int) bool {
	for i := 2; i <= n-2; i++ {
		if !isPalindrom(baseConvert(i, n)) {
			return false
		}
	}

	return true
}

func main() {
	fmt.Println(isStrictlyPalindromic(9))
	fmt.Println(isStrictlyPalindromic(4))
}
