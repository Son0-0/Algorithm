package main

import "fmt"

func mergeAlternately(word1 string, word2 string) string {
	result := ""

	lenA, lenB := len(word1), len(word2)
	cnt := 0

	for cnt < lenA && cnt < lenB {
		result = result + string(word1[cnt]) + string(word2[cnt])
		cnt++
	}

	if lenA < lenB {
		for cnt < lenB {
			result += string(word2[cnt])
			cnt++
		}
	} else if lenB < lenA {
		for cnt < lenA {
			result += string(word1[cnt])
			cnt++
		}
	}

	return result
}

func main() {
	fmt.Println(mergeAlternately("abc", "pqr"))
	fmt.Println(mergeAlternately("ab", "pqrs"))
	fmt.Println(mergeAlternately("abcd", "pq"))
}
