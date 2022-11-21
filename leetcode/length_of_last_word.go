package main

import (
	"fmt"
)

func lengthOfLastWord(s string) int {
	length := len(s) - 1

	result := 0

	for i := length; i >= 0; i-- {
		if result != 0 && string(s[i]) == " " {
			break
		} else if string(s[i]) != " " {
			result += 1
		}
	}

	return result
}

func main() {
	fmt.Println(lengthOfLastWord("Hello World"))
	fmt.Println(lengthOfLastWord("   fly me   to   the moon  "))
	fmt.Println(lengthOfLastWord("luffy is still joyboy"))
}
