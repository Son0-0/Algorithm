package main

import "fmt"

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func commonFactors(a int, b int) int {
	target, cnt := min(a, b), 1

	for i := 2; i <= target; i++ {
		if a%i == 0 && b%i == 0 {
			cnt++
		}
	}

	return cnt
}

func main() {
	fmt.Println(commonFactors(12, 6))
	fmt.Println(commonFactors(25, 30))
}
