package main

import "fmt"

func shortestPathBinaryMatrix(grid [][]int) int {
	n := len(grid)

	if grid[0][0] == 1 || grid[n-1][n-1] == 1 {
		return -1
	}

	result := 10001

	dx, dy := []int{-1, -1, 0, 1, 1, 1, 0, -1}, []int{0, 1, 1, 1, 0, -1, -1, -1}

	q := make([][]int, 0)

	q = append(q, []int{0, 0})
	grid[0][0] = 1

	for len(q) != 0 {
		cur := q[0]
		q = q[1:]

		cx, cy := cur[0], cur[1]

		if cx == n-1 && cy == n-1 {
			if grid[cx][cy] < result {
				result = grid[cx][cy]
			}
		}

		for i := 0; i < 8; i++ {
			nx, ny := cx+dx[i], cy+dy[i]
			if (0 <= nx && nx < n) && (0 <= ny && ny < n) {
				if grid[nx][ny] == 0 {
					q = append(q, []int{nx, ny})
					grid[nx][ny] = grid[cx][cy] + 1
				}
			}
		}
	}

	if grid[n-1][n-1] == 0 {
		result = -1
	}

	return result
}

func main() {
	fmt.Println(shortestPathBinaryMatrix([][]int{{0, 1}, {1, 0}}))
	fmt.Println(shortestPathBinaryMatrix([][]int{{0, 0, 0}, {1, 1, 0}, {1, 1, 0}}))
	fmt.Println(shortestPathBinaryMatrix([][]int{{1, 0, 0}, {1, 1, 0}, {1, 1, 0}}))
}
