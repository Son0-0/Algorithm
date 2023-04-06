package main

import "fmt"

func closedIsland(grid [][]int) int {
	result := 0

	row, col := len(grid), len(grid[0])

	dx, dy := []int{0, -1, 0, 1}, []int{-1, 0, 1, 0}

	var dfs func(int, int) int

	dfs = func(x, y int) int {
		if (0 > x || row <= x) || (0 > y || col <= y) {
			return 0
		}

		if grid[x][y] == 1 {
			return 1
		}

		grid[x][y] = 1

		result := 1
		for i := 0; i < 4; i++ {
			result *= dfs(x+dx[i], y+dy[i])
		}

		return result
	}

	for i := 0; i < row; i++ {
		for j := 0; j < col; j++ {
			if grid[i][j] == 0 && dfs(i, j) == 1 {
				result++
			}
		}
	}

	return result
}

func main() {
	fmt.Println(closedIsland([][]int{{0, 0, 1, 0, 0}, {0, 1, 0, 1, 0}, {0, 1, 1, 1, 0}}))
}
