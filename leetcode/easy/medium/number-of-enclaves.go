package main

import "fmt"

func numEnclaves(grid [][]int) int {
	result := 0
	row, col := len(grid), len(grid[0])

	dx, dy := []int{0, -1, 0, 1}, []int{-1, 0, 1, 0}

	var erase func(int, int, int)

	erase = func(x, y, opt int) {
		if opt == 1 {
			result++
		}

		grid[x][y] = -1

		for i := 0; i < 4; i++ {
			nx, ny := x+dx[i], y+dy[i]

			if (0 <= nx && nx < row) && (0 <= ny && ny < col) {
				if grid[nx][ny] == 1 {
					erase(nx, ny, opt)
				}
			}
		}
	}

	for i := 0; i < row; i++ {
		for j := 0; j < col; j++ {
			if i == 0 || i == row-1 || j == 0 || j == col-1 {
				if grid[i][j] == 1 {
					erase(i, j, 0)
				}
			}
		}
	}

	for i := 0; i < row; i++ {
		for j := 0; j < col; j++ {
			if grid[i][j] == 1 {
				erase(i, j, 1)
			}
		}
	}

	return result
}

func main() {
	fmt.Println(numEnclaves([][]int{{0, 0, 0, 0}, {1, 0, 1, 0}, {0, 1, 1, 0}, {0, 0, 0, 0}}))
}
