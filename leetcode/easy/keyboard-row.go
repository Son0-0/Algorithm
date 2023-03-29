package main

import "strings"

func findWords(words []string) []string {
	result := []string{}
	dict := make(map[rune]int)

	for _, c := range "qwertyuiop" {
		dict[c] = 1
	}

	for _, c := range "asdfghjkl" {
		dict[c] = 2
	}

	for _, c := range "zxcvbnm" {
		dict[c] = 3
	}

	var isValid func(string) bool

	isValid = func(target string) bool {
		start := target[0]

		for _, c := range target {
			if dict[c] != dict[rune(start)] {
				return false
			}
		}

		return true
	}

	for _, word := range words {
		if isValid(strings.ToLower(word)) {
			result = append(result, word)
		}
	}

	return result
}
