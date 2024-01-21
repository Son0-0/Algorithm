package main

import (
	"fmt"
	"strconv"
)

func smallestNumber(pattern string) string {
	result, stack := "", []int{}

	length := len(pattern)

	for idx, p := range pattern + " " {
		stack = append(stack, idx+1)

		if idx == length || p == 'I' {
			for len(stack) != 0 {
				result += strconv.Itoa(stack[len(stack)-1])
				stack = stack[:len(stack)-1]
			}
		}
	}

	return result
}

// Backtracking
// func check(target, pattern string) bool {

// 	for idx, p := range pattern {
// 		n1, _ := strconv.Atoi(string(target[idx]))
// 		n2, _ := strconv.Atoi(string(target[idx+1]))

// 		if p == 'I' {
// 			if n2 < n1 {
// 				return false
// 			}
// 		} else {
// 			if n1 < n2 {
// 				return false
// 			}
// 		}
// 	}

// 	return true
// }

// func smallestNumber(pattern string) string {
// 	result := "9999999999"

// 	length := len(pattern) + 1

// 	var dfs func(int, map[int]bool, string)

// 	dfs = func(cur int, visited map[int]bool, s string) {
// 		if result != "9999999999" {
// 			return
// 		}

// 		if len(s) == length {
// 			if check(s, pattern) {
// 				if s < result {
// 					result = s
// 				}
// 			}
// 			return
// 		}

// 		for i := 1; i <= length; i++ {
// 			if _, e := visited[i]; !e {
// 				visited[i] = true
// 				dfs(i, visited, s+strconv.Itoa(i))
// 				delete(visited, i)
// 			}
// 		}
// 	}

// 	dfs(0, make(map[int]bool), "")

// 	return result
// }

func main() {
	fmt.Println(smallestNumber("IIIDIDDD"))
	fmt.Println(smallestNumber("DDD"))
}
