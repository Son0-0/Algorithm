package main

import "fmt"

func max(a, b int) int {
	if a < b {
		return b
	}
	return a
}

func numOfMinutes(n int, headID int, manager []int, informTime []int) int {
	result := 0

	graph := make([][]int, n)

	for i, m := range manager {
		if m == -1 {
			continue
		}
		graph[m] = append(graph[m], i)
	}

	var dfs func(int, int)

	visited := make([]int, n)

	dfs = func(cur, time int) {
		result = max(result, time)

		for _, node := range graph[cur] {
			if visited[node] == 0 {
				visited[node] = 1
				dfs(node, time+informTime[node])
			}
		}
	}

	dfs(headID, informTime[headID])

	return result
}

func main() {
	fmt.Println(numOfMinutes(1, 0, []int{-1}, []int{0}))
	fmt.Println(numOfMinutes(6, 2, []int{2, 2, -1, 2, 2, 2}, []int{0, 0, 1, 0, 0, 0}))
	fmt.Println(numOfMinutes(10, 2, []int{2, 2, -1, 2, 2, 2, 1, 1, 6, 7}, []int{0, 1, 1, 0, 0, 0, 3, 4, 0, 0}))
}
