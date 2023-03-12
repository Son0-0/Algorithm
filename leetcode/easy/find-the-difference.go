package main

import "fmt"

func findTheDifference(s string, t string) byte {
	var result byte

	for i := 0; i < len(t); i++ {
		result += t[i]
	}

	for i := 0; i < len(s); i++ {
		result -= s[i]
	}

	return result
}

// func findTheDifference(s string, t string) byte {
// 	diff := make(map[byte]int)

// 	for _, c := range t {
// 		diff[byte(c)]++
// 	}

// 	for _, c := range s {
// 		diff[byte(c)]--
// 	}

// 	for key := range diff {
// 		if diff[key] != 0 {
// 			return key
// 		}
// 	}

// 	return byte(0)
// }

func main() {
	fmt.Println(findTheDifference("abcd", "abcde"))
}
