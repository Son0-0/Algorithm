package main

import "fmt"

func countSubIslands(grid1 [][]int, grid2 [][]int) int {
	result := 0

	row, col := len(grid1), len(grid1[0])
	dx, dy := []int{-1, 0, 1, 0}, []int{0, 1, 0, -1}

	parents := make([][]int, row)

	// init parents 2d-slice
	for i := 0; i < row; i++ {
		for j := 0; j < col; j++ {
			parents[i] = append(parents[i], 0)
		}
	}

	var dfs func(int, int, int)

	dfs = func(x, y, cur int) {
		parents[x][y] = cur
		grid1[x][y] = -1

		for i := 0; i < 4; i++ {
			nx, ny := x+dx[i], y+dy[i]

			if (0 <= nx && nx < row) && (0 <= ny && ny < col) {
				if grid1[nx][ny] == 1 {
					dfs(nx, ny, cur)
				}
			}
		}
	}

	cur := 1
	for i := 0; i < row; i++ {
		for j := 0; j < col; j++ {
			if grid1[i][j] == 1 {
				dfs(i, j, cur)
				cur++
			}
		}
	}

	valid := true

	var check func(int, int, int)

	check = func(x, y, cur int) {

		grid2[x][y] = -1

		for i := 0; i < 4; i++ {
			nx, ny := x+dx[i], y+dy[i]

			if (0 <= nx && nx < row) && (0 <= ny && ny < col) {
				if grid2[nx][ny] == 1 {
					if parents[nx][ny] != cur {
						valid = false
					}
					check(nx, ny, cur)
				}
			}
		}
	}

	for i := 0; i < row; i++ {
		for j := 0; j < col; j++ {
			if grid2[i][j] == 1 && 0 < parents[i][j] {
				valid = true
				check(i, j, parents[i][j])
				if valid == true {
					result++
				}
			}
		}
	}

	return result
}

func main() {
	fmt.Println(countSubIslands([][]int{{1, 1, 1, 0, 0}, {0, 1, 1, 1, 1}, {0, 0, 0, 0, 0}, {1, 0, 0, 0, 0}, {1, 1, 0, 1, 1}}, [][]int{{1, 1, 1, 0, 0}, {0, 0, 1, 1, 1}, {0, 1, 0, 0, 0}, {1, 0, 1, 1, 0}, {0, 1, 0, 1, 0}}))
}
