package main

import (
	"fmt"
	"strings"
)

func isVowel(target byte) bool {
	for _, c := range "aAeEiIoOuU" {
		if target == byte(c) {
			return true
		}
	}

	return false
}

func check(target string, index int) string {
	start := target[0]
	result := ""

	if isVowel(start) {
		result = target + "ma"
	} else {
		result = target[1:] + string(start) + "ma"
	}

	for index != 0 {
		result += "a"
		index--
	}

	return result
}

func toGoatLatin(sentence string) string {
	result := ""

	for i, word := range strings.Split(sentence, " ") {
		result += check(word, i+1) + " "
	}

	return result[:len(result)-1]
}

func main() {
	fmt.Println(toGoatLatin("I speak Goat Latin"))
	fmt.Println(toGoatLatin("The quick brown fox jumped over the lazy dog"))
	fmt.Println(toGoatLatin("Each word consists of lowercase and uppercase letters only"))
}
