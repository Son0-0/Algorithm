package main

import "fmt"

func findCircleNum(isConnected [][]int) int {
	result := 0

	visited := make([]int, len(isConnected))

	var dfs func(int)

	dfs = func(cur int) {
		for idx, v := range isConnected[cur] {
			if idx == cur {
				continue
			} else {
				if v == 1 && visited[idx] == 0 {
					visited[idx] = 1
					dfs(idx)
				}
			}
		}
	}

	for i := 0; i < len(isConnected); i++ {
		if visited[i] == 0 {
			visited[i] = 1
			dfs(i)
			result++
		}
	}

	return result
}

func main() {
	fmt.Println(findCircleNum([][]int{{1, 1, 0}, {1, 1, 0}, {0, 0, 1}}))
	fmt.Println(findCircleNum([][]int{{1, 0, 0}, {0, 1, 0}, {0, 0, 1}}))
	// [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
	fmt.Println(findCircleNum([][]int{{1, 0, 0, 1}, {0, 1, 1, 0}, {0, 1, 1, 1}, {1, 0, 1, 1}}))

}
