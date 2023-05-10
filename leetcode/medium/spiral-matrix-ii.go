package main

import "fmt"

type node struct {
	x int
	y int
}

func generateMatrix(n int) [][]int {
	result := make([][]int, n)

	for i := 0; i < n; i++ {
		temp := make([]int, n)
		result[i] = temp
	}

	dir := [][]int{{0, 1}, {1, 0}, {0, -1}, {-1, 0}}
	curDir := 0
	cx, cy := 0, 0

	visited := make(map[node]bool)
	visited[node{x: cx, y: cy}] = true
	result[cx][cy] = 1

	cnt := 2

	for cnt <= n*n {
		nx, ny := cx+dir[curDir][0], cy+dir[curDir][1]

		if (0 <= nx && nx < n) && (0 <= ny && ny < n) {
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

		result[cx][cy] = cnt

		cnt++
	}

	return result
}

func main() {
	fmt.Println(generateMatrix(3))
	fmt.Println(generateMatrix(1))
}
