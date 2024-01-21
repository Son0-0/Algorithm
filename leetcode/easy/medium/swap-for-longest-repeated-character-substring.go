package main

import "fmt"

func max(a, b int) int {
	if a < b {
		return b
	}
	return a
}

func maxRepOpt1(text string) int {
	alpha := make(map[rune]int)

	for _, c := range text {
		if _, e := alpha[c]; e {
			alpha[c] += 1
		} else {
			alpha[c] = 1
		}
	}

	result := 0
	for i := 0; i < len(text); i++ {
		target := text[i] // 비교할 alpha
		chance := 0       // 1번 swap 가능
		cur := i + 1      // 비교 대상
		length := 1       // 현재 길이

		alphaCnt := alpha[rune(target)] - 1

		for cur < len(text) {
			if target != text[cur] {
				if chance == 0 {
					chance += 1
				} else {
					break
				}
			} else {
				alphaCnt -= 1
			}

			length += 1
			cur += 1
		}

		if chance <= alphaCnt {
			// 조건 정리 필요
			if chance == 0 && (0 < i-1 || i+length < len(text)) && (alphaCnt > 0) {
				result = max(result, length+1)
			} else {
				result = max(result, length)
			}
		} else {
			result = max(result, length-1)
		}
	}

	return result
}

func main() {
	fmt.Println(maxRepOpt1("abcdef"))
	// fmt.Println(maxRepOpt1("acbaaa"))
	// fmt.Println(maxRepOpt1("bbababaaaa"))
	// fmt.Println(maxRepOpt1("aaabbaaa"))
	// fmt.Println(maxRepOpt1("ababa"))
	// fmt.Println(maxRepOpt1("aaabaaa"))
	// fmt.Println(maxRepOpt1("aaaaa"))
}

// for Debug
// fmt.Printf("length: %d cur: %d chance: %d alphaCnt: %d\n", length, cur, chance, alphaCnt)
