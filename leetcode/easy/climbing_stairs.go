package main

import "fmt"

func climbStairs(n int) int {
	stairs := []int{1, 1}

	for i := 2; i <= n; i++ {
		stairs = append(stairs, stairs[i-1]+stairs[i-2])
	}

	return stairs[n]
}

func main() {
	fmt.Println(climbStairs(2))
	fmt.Println(climbStairs(3))
}
