package main

import "fmt"

func main() {
	var dp [101]int
	dp[1] = 1
	dp[2] = 1
	dp[3] = 1
	dp[4] = 2

	var t int
	fmt.Scanf("%d", &t)

	for i := 0; i < t; i++ {
		var n int
		fmt.Scanf("%d", &n)
		if dp[n] != 0 {
			fmt.Println(dp[n])
		} else {
			for j := 5; j < n+1; j++ {
				dp[j] = dp[j-2] + dp[j-3]
			}
			fmt.Println(dp[n])
		}
	}
}
