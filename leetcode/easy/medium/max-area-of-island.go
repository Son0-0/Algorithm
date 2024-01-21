package main

import "fmt"

func max(a, b int) int {
	if a < b {
		return b
	}
	return a
}

func maxAreaOfIsland(grid [][]int) int {
	result := 0
	row, col := len(grid), len(grid[0])

	dx, dy := []int{0, 1, 0, -1}, []int{-1, 0, 1, 0}

	var dfs func(int, int) int

	dfs = func(x, y int) int {
		if grid[x][y] == 0 {
			return 0
		}

		grid[x][y] = 0

		area := 1

		for i := 0; i < 4; i++ {
			nx, ny := x+dx[i], y+dy[i]

			if (0 <= nx && nx < row) && (0 <= ny && ny < col) {
				if grid[nx][ny] == 1 {
					area += dfs(nx, ny)
				}
			}
		}

		return area
	}

	for i := 0; i < row; i++ {
		for j := 0; j < col; j++ {
			if grid[i][j] == 1 {
				result = max(result, dfs(i, j))
			}
		}
	}

	return result
}

func main() {
	fmt.Println(maxAreaOfIsland([][]int{{1, 1, 0, 0, 0}, {1, 1, 0, 0, 0}, {0, 0, 0, 1, 1}, {0, 0, 0, 1, 1}}))
	fmt.Println(maxAreaOfIsland([][]int{{0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0}, {0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0}, {0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0}, {0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0}, {0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0}, {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0}, {0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0}, {0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0}}))
	fmt.Println(maxAreaOfIsland([][]int{{0, 0, 0, 0, 0, 0, 0, 0}}))
	fmt.Println(maxAreaOfIsland([][]int{{0, 0, 0, 0, 0, 0, 0, 1}}))
}
