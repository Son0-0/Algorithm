package main

import (
	"bufio"
	"os"
	"strconv"
	"strings"
)

func main() {
	sc := bufio.NewScanner(os.Stdin)
	wr := bufio.NewWriter(os.Stdout)

	sc.Scan()
	n, _ := strconv.Atoi(sc.Text())

	dp := make([]int, n+1)

	sc.Scan()
	s := sc.Text()
	slice := strings.Split(s, " ")

	for i, str := range slice {
		dp[i+1], _ = strconv.Atoi(str)
	}

	for i := 2; i <= n; i++ {
		for j := 1; j < i; j++ {
			target := dp[i-j] + dp[j]
			if dp[i] < target {
				dp[i] = target
			}
		}
	}

	wr.WriteString(strconv.Itoa(dp[n]))
	wr.Flush()
}
