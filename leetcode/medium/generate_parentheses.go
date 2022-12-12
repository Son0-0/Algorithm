package main

import "fmt"

func generateParenthesis(n int) []string {
	var dfs func(int, int, string)

	result := make([]string, 0)

	dfs = func(left int, right int, str string) {
		if len(str) == n*2 {
			result = append(result, str)
		}

		if left < n {
			dfs(left+1, right, str+"(")
		}

		if right < left {
			dfs(left, right+1, str+")")
		}
	}

	dfs(1, 0, "(")

	return result
}

func main() {
	fmt.Println(generateParenthesis(3))
	fmt.Println(generateParenthesis(1))
}
