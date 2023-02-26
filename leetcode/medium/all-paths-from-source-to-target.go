package main

import "fmt"

func allPathsSourceTarget(graph [][]int) [][]int {
	result := [][]int{}

	target := len(graph) - 1

	var dfs func(int, int, map[int]int)

	dfs = func(cur, order int, visited map[int]int) {
		if cur == target {
			temp := make([]int, len(visited))
			for key := range visited {
				temp[visited[key]] = key
			}
			result = append(result, temp)
			return
		}

		for _, node := range graph[cur] {
			if _, e := visited[node]; !e {
				visited[node] = order + 1
				dfs(node, order+1, visited)
				delete(visited, node)
			}
		}

	}

	dfs(0, 0, map[int]int{0: 0})

	return result
}

func main() {
	fmt.Println(allPathsSourceTarget([][]int{{1, 2}, {3}, {3}, {}}))
	fmt.Println(allPathsSourceTarget([][]int{{4, 3, 1}, {3, 2, 4}, {3}, {4}, {}}))
}
