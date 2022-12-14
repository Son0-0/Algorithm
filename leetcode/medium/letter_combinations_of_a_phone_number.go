package main

import (
	"fmt"
)

func letterCombinations(digits string) []string {
	phone := make(map[string][]string, 8)
	cur := 0

	for i := 0; i <= 7; i++ {
		temp := string('2' + i)
		for j := 0; j < 3; j++ {
			phone[temp] = append(phone[temp], string('a'+cur))
			cur += 1
		}

		if temp == "7" || temp == "9" {
			phone[temp] = append(phone[temp], string('a'+cur))
			cur += 1
		}
	}

	var dfs func(int, string)
	length := len(digits)
	result := []string{}

	dfs = func(cur int, visited string) {
		if cur == length {
			result = append(result, visited)
			return
		}

		for _, s := range phone[string(digits[cur])] {
			dfs(cur+1, visited+s)
		}
	}

	if len(digits) == 0 {
		return result
	}

	dfs(0, "")

	return result
}

func main() {
	fmt.Println(letterCombinations("23"))
	fmt.Println(letterCombinations(""))
	fmt.Println(letterCombinations("2"))
}
