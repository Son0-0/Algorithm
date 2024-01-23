package main

import "fmt"

func max(a, b int) int {
	if a < b {
		return b
	}
	return a
}

func maxLength(arr []string) int {
	result := 0
	size := len(arr)

	var dfs func(int, int, map[rune]int)

	dfs = func(i, length int, m map[rune]int) {
		for idx := i + 1; idx < size; idx++ {
			tempString := arr[idx]

			flag := true

			for _, chr := range tempString {
				if v, e := m[rune(chr)]; e {
					if v > 0 {
						flag = false
						break
					}
				}
			}

			if flag {
				for _, chr := range tempString {
					m[rune(chr)] += 1
					if m[rune(chr)] > 1 {
						flag = false
					}
				}

				if flag {
					curLength := length + len(tempString)
					result = max(result, curLength)
					dfs(idx, curLength, m)
				}

				for _, chr := range tempString {
					m[rune(chr)] -= 1
				}
			}
		}
	}

	for i := 0; i < size; i++ {
		m := make(map[rune]int)
		flag := true
		for _, chr := range arr[i] {
			m[rune(chr)] += 1

			if m[rune(chr)] > 1 {
				flag = false
				break
			}
		}

		if flag {
			result = max(result, len(arr[i]))
			dfs(i, len(arr[i]), m)
		}
	}

	return result
}

func main() {
	// parameter := []string{"un", "iq", "ue"}
	// parameter := []string{"cha", "r", "act", "ers"}
	// parameter := []string{"abcdefghijklmnopqrstuvwxyz"}
	parameter := []string{"e", "tpgynpylqbyqjaf", "svkgfmpgftxjjrcxxsog", "bxypbbrlckiolfwpqgsoc", "kwnelumrnnsryjdeppanuqbsu"}
	result := maxLength(parameter)

	fmt.Println("result: ", result)
}
