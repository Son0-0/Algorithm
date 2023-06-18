package main

import "fmt"

func pow(a, b int) int {
	result := 1

	for i := 0; i < b; i++ {
		result *= a
	}

	return result
}

func countPaths(grid [][]int) int {
	mod := pow(10, 9) + 7
	result := 0

	row, col := len(grid), len(grid[0])

	dx := []int{0, 1, 0, -1}
	dy := []int{1, 0, -1, 0}

	dp := make([][]int, row)
	for i := 0; i < row; i++ {
		dp[i] = make([]int, col)
	}

	var dfs func(int, int) int

	dfs = func(x, y int) int {
		if 0 < dp[x][y] {
			return dp[x][y]
		}

		cnt := 1

		for i := 0; i < 4; i++ {
			nx, ny := x+dx[i], y+dy[i]

			if (0 <= nx && nx < row) && (0 <= ny && ny < col) {
				if grid[x][y] < grid[nx][ny] {
					cnt = (cnt + dfs(nx, ny)) % mod
				}
			}
		}

		dp[x][y] = cnt
		return cnt
	}

	for i := 0; i < row; i++ {
		for j := 0; j < col; j++ {
			result = (result + dfs(i, j)) % mod
		}
	}

	return result
}

func main() {
	fmt.Println(countPaths([][]int{{1, 1}, {3, 4}}))
}
