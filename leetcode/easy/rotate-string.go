package main

import "fmt"

func rotateString(s string, goal string) bool {
	result := false

	cnt, size := 0, len(s)

	for cnt != size {
		if s == goal {
			return true
		}
		s = s[1:] + string(s[0])
		cnt++
	}

	return result
}

func main() {
	fmt.Println(rotateString("abcde", "cdeab"))
	fmt.Println(rotateString("abcde", "abced"))
}
