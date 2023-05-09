package main

import "fmt"

type node struct {
	x int
	y int
}

func spiralOrder(matrix [][]int) []int {
	result := make([]int, 0)
	row, col := len(matrix), len(matrix[0])
	visited := make(map[node]bool)

	dir := [][]int{{0, 1}, {1, 0}, {0, -1}, {-1, 0}}
	curDir := 0
	cx, cy := 0, 0

	result = append(result, matrix[cx][cy])
	visited[node{x: cx, y: cy}] = true
	cnt := 1

	for cnt < row*col {
		nx, ny := cx+dir[curDir][0], cy+dir[curDir][1]

		if (0 <= nx && nx < row) && (0 <= ny && ny < col) {
			if _, e := visited[node{x: nx, y: ny}]; e {
				curDir = (curDir + 1) % 4
				nx, ny = cx+dir[curDir][0], cy+dir[curDir][1]
			}
		} else {
			curDir = (curDir + 1) % 4
			nx, ny = cx+dir[curDir][0], cy+dir[curDir][1]
		}

		cx, cy = nx, ny

		visited[node{x: cx, y: cy}] = true

		result = append(result, matrix[cx][cy])

		cnt++
	}

	return result
}

func main() {
	fmt.Println(spiralOrder([][]int{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}))
	fmt.Println(spiralOrder([][]int{{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}}))
}
