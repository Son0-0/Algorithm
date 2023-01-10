package main

import "fmt"

func max(a, b int) int {
	if a < b {
		return b
	}
	return a
}

func maxLengthBetweenEqualCharacters(s string) int {
	alpha := make(map[byte][]int)

	for index, c := range s {
		if _, exists := alpha[byte(c)]; exists {
			alpha[byte(c)] = append(alpha[byte(c)], index)
		} else {
			alpha[byte(c)] = []int{index}
		}
	}

	result := -1
	for key := range alpha {
		if len(alpha[key]) > 1 {
			result = max(result, alpha[key][len(alpha[key])-1]-alpha[key][0]-1)
		}
	}

	return result
}

// brute force
// func maxLengthBetweenEqualCharacters(s string) int {
// 	result := -1

// 	for i, c := range s {
// 		cur := byte(c)

// 		for j := len(s) - 1; j > 0; j-- {
// 			if j-i-1 < result {
// 				break
// 			}

// 			if s[j] == cur {
// 				result = max(result, j-i-1)
// 			}
// 		}
// 	}

// 	return result
// }

func main() {
	fmt.Println(maxLengthBetweenEqualCharacters("aa"))
	fmt.Println(maxLengthBetweenEqualCharacters("abca"))
	fmt.Println(maxLengthBetweenEqualCharacters("cbzxy"))
}
