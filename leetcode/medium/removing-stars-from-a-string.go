package main

import (
	"fmt"
	"strings"
)

func removeStars(s string) string {
	stack := make([]string, len(s))
	top := 0

	for _, c := range s {
		if c != '*' {
			stack[top] = string(c)
			top++
		} else {
			top--
		}
	}

	return strings.Join(stack[:top], "")
}

func main() {
	fmt.Println(removeStars("leet**cod*e"))
	fmt.Println(removeStars("erase*****"))
}
