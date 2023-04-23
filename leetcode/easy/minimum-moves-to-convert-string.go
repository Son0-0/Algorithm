package main

import "fmt"

func minimumMoves(s string) int {
	result := 0
	size, pos := len(s), 0

	for pos < size {
		if s[pos] == 'X' {
			result++
			pos += 3
		} else {
			pos++
		}
	}

	return result
}

func main() {
	fmt.Println(minimumMoves("XXX"))
	fmt.Println(minimumMoves("XXOX"))
}
