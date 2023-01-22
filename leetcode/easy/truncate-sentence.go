package main

import (
	"fmt"
	"strings"
)

func truncateSentence(s string, k int) string {
	result := ""
	str := strings.Split(s, " ")

	for i, s := range str {
		if i < k {
			result += string(s) + " "
		}
	}

	return result[:len(result)-1]
}

func main() {
	fmt.Println(truncateSentence("Hello how are you Contestant", 4))
	fmt.Println(truncateSentence("What is the solution to this problem", 4))
	fmt.Println(truncateSentence("chopper is not a tanuki", 5))
}
