package main

import "fmt"

func nextGreatestLetter(letters []byte, target byte) byte {
	for _, c := range letters {
		if target < c {
			return c
		}
	}

	return letters[0]
}

func main() {
	fmt.Println(nextGreatestLetter([]byte{'c', 'f', 'j'}, 'a'))
	fmt.Println(nextGreatestLetter([]byte{'c', 'f', 'j'}, 'c'))
	fmt.Println(nextGreatestLetter([]byte{'x', 'x', 'y', 'y'}, 'z'))
}
