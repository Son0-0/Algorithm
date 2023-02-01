package main

import "fmt"

func max(a, b int) int {
	if a < b {
		return b
	}
	return a
}

func min(a, b int) int {
	if b < a {
		return b
	}
	return a
}

func canReach(s string, minJump int, maxJump int) bool {
	queue := []int{}
	queue = append(queue, 0)

	mv := -1

	for len(queue) != 0 {
		cur := queue[0]
		queue = queue[1:]

		for i := max(cur+minJump, mv+1); i <= min(cur+maxJump, len(s)-1); i++ {
			if s[i] == '0' {
				if i == len(s)-1 {
					return true
				}
				queue = append(queue, i)
			}
		}
		mv = cur + maxJump
	}

	return false
}

func main() {
	fmt.Println(canReach("01", 1, 1))
	fmt.Println(canReach("011010", 2, 3))
	fmt.Println(canReach("01101110", 2, 3))
}
