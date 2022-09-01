package main

import "fmt"

func main() {
	var N int
	fmt.Scanf("%d", &N)

	dp := make([][]int, N+1)
	for i := range dp {
		dp[i] = make([]int, 10)
	}

	for i := 1; i < 10; i++ {
		dp[1][i] = 1
	}

	mod := 1000000000

	for i := 2; i <= N; i++ {
		for j := 0; j < 10; j++ {
			if j == 0 {
				dp[i][0] = dp[i-1][1] % mod
			} else if j == 9 {
				dp[i][9] = dp[i-1][8] % mod
			} else {
				dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % mod
			}
		}
	}

	answer := 0

	for _, num := range dp[N] {
		answer += num % mod
	}
	fmt.Println(answer % mod)
}
