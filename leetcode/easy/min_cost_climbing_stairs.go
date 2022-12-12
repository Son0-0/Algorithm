package main

import "fmt"

func minCostClimbingStairs(cost []int) int {
	length := len(cost)
	m, n, k := 0, 0, 0

	for i := 2; i <= length; i++ {
		t1, t2 := m+cost[i-2], n+cost[i-1]
		if t1 < t2 {
			k = t1
		} else {
			k = t2
		}

		m = n
		n = k
	}

	return k
}

func main() {
	fmt.Println(minCostClimbingStairs([]int{10, 15, 20}))
	fmt.Println(minCostClimbingStairs([]int{1, 100, 1, 1, 1, 100, 1, 1, 100, 1}))
}
