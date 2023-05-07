package main

import "fmt"

func numIdenticalPairs(nums []int) int {
	size := len(nums)
	result := 0

	var dfs func(int, int, []int)

	dfs = func(cur, length int, visited []int) {
		if length == 2 {
			if nums[visited[0]] == nums[visited[1]] {
				result++
			}
			return
		}

		for i := cur + 1; i < size; i++ {
			dfs(i, length+1, append(visited, i))
		}
	}

	dfs(-1, 0, []int{})

	return result
}

func main() {
	fmt.Println(numIdenticalPairs([]int{1, 2, 3, 1, 1, 3}))
	fmt.Println(numIdenticalPairs([]int{1, 1, 1, 1}))
	fmt.Println(numIdenticalPairs([]int{1, 2, 3}))
}
