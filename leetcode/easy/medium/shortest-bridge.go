package main

import "fmt"

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func shortestBridge(grid [][]int) int {
	result := 101
	n := len(grid)

	dx, dy := []int{-1, 0, 1, 0}, []int{0, 1, 0, -1}

	var dfs func(int, int)

	dfs = func(x, y int) {
		if grid[x][y] == 0 {
			return
		}

		grid[x][y] = -1

		for i := 0; i < 4; i++ {
			nx, ny := x+dx[i], y+dy[i]

			if (0 <= nx && nx < n) && (0 <= ny && ny < n) {
				if grid[nx][ny] == 1 {
					dfs(nx, ny)
				}
			}
		}
	}

	flag := 0
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			if grid[i][j] == 1 {
				dfs(i, j)
				flag = 1
				break
			}
		}
		if flag == 1 {
			break
		}
	}

	var bfs func(int, int)

	bfs = func(x, y int) {
		q := [][]int{}

		q = append(q, []int{x, y, 1})

		for len(q) != 0 {
			cur := q[0]
			q = q[1:]

			for i := 0; i < 4; i++ {
				nx, ny := cur[0]+dx[i], cur[1]+dy[i]

				if (0 <= nx && nx < n) && (0 <= ny && ny < n) {
					if grid[nx][ny] == -1 {
						result = min(result, cur[2])
					}

					if (grid[nx][ny] == 0) || (cur[2]+1 < grid[nx][ny]) {
						grid[nx][ny] = cur[2] + 1
						q = append(q, []int{nx, ny, cur[2] + 1})
					}
				}
			}
		}
	}

	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			if grid[i][j] == 1 {
				bfs(i, j)
			}
		}
	}

	return result - 1
}

func main() {
	fmt.Println(shortestBridge([][]int{{0, 1}, {1, 0}}))
	fmt.Println(shortestBridge([][]int{{0, 1, 0}, {0, 0, 0}, {0, 0, 1}}))
	fmt.Println(shortestBridge([][]int{{1, 1, 1, 1, 1}, {1, 0, 0, 0, 1}, {1, 0, 1, 0, 1}, {1, 0, 0, 0, 1}, {1, 1, 1, 1, 1}}))
}
