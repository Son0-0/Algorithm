package main

import (
	"fmt"
	"sort"
)

func max(a, b int) int {
	if a < b {
		return b
	}
	return a
}

func makesquare(matchsticks []int) bool {
	num := make(map[int]int)
	sum := 0
	maxValue := 0

	for _, matchstick := range matchsticks {
		if _, exists := num[matchstick]; exists {
			num[matchstick] += 1
		} else {
			num[matchstick] = 1
		}

		sum += matchstick
		maxValue = max(maxValue, matchstick)
	}

	target := sum / 4

	if sum < 4 || sum%4 != 0 || target < maxValue {
		return false
	}

	sort.SliceStable(matchsticks, func(a, b int) bool {
		if b < a {
			return true
		}
		return false
	})

	result := make([]int, 4)
	var dfs func(int) bool

	dfs = func(cur int) bool {
		if cur == len(matchsticks) {
			return result[0] == result[1] && result[1] == result[2] && result[2] == target
		}

		for i := 0; i < 4; i++ {
			if result[i]+matchsticks[cur] <= target {
				result[i] += matchsticks[cur]
				if dfs(cur + 1) {
					return true
				}
				result[i] -= matchsticks[cur]
			}
		}

		return false
	}

	return dfs(0)
}

func main() {
	fmt.Println(makesquare([]int{1, 1, 1, 2, 2, 2, 3}))
	fmt.Println(makesquare([]int{1, 1, 2, 2, 2}))
	fmt.Println(makesquare([]int{3, 3, 3, 3, 4}))
}
