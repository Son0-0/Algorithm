package main

import (
	"fmt"
	"strconv"
)

func isPalindrome(x int) bool {
	target := strconv.Itoa(x)

	length := len(target) - 1
	half := len(target) / 2

	for i := 0; i < half; i++ {
		if target[i] != target[length-i] {
			return false
		}
	}

	return true
}

func main() {
	fmt.Println(isPalindrome(121))
	fmt.Println(isPalindrome(-121))
	fmt.Println(isPalindrome(10))
}
