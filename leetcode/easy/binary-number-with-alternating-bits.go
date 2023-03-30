package main

import (
	"fmt"
	"strconv"
)

func hasAlternatingBits(n int) bool {
	target := strconv.FormatInt(int64(n), 2)
	cur := target[0]

	for i := 1; i < len(target); i++ {
		if target[i] == cur {
			return false
		} else {
			cur = target[i]
		}
	}

	return true
}

func main() {
	fmt.Println(hasAlternatingBits(5))
	fmt.Println(hasAlternatingBits(7))
	fmt.Println(hasAlternatingBits(11))
}
