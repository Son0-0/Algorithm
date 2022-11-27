package main

import (
	"fmt"
	"sort"
)

func minimumCost(cost []int) int {
	result := 0

	sort.Ints(cost)

	candy := 0
	for i := len(cost) - 1; i >= 0; i-- {
		if candy == 2 {
			candy = 0
		} else {
			result += cost[i]
			candy += 1
		}
	}

	return result
}

func main() {
	fmt.Println(minimumCost([]int{1, 2, 3}))
	fmt.Println(minimumCost([]int{6, 5, 7, 9, 2, 2}))
	fmt.Println(minimumCost([]int{5, 5}))
}
