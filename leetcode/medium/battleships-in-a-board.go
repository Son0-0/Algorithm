package main

import (
	"fmt"
)

func countBattleships(board [][]byte) int {
	result := 0

	xlen, ylen := len(board), len(board[0])

	var dfs func(int, int)

	dx, dy := []int{-1, 0, 1, 0}, []int{0, 1, 0, -1}

	dfs = func(x, y int) {
		for i := 0; i < 4; i++ {
			nx, ny := x+dx[i], y+dy[i]
			if (0 <= nx && nx < xlen) && (0 <= ny && ny < ylen) && board[nx][ny] == 'X' {
				board[nx][ny] = '.'
				dfs(nx, ny)
			}
		}
	}

	for x := 0; x < xlen; x++ {
		for y := 0; y < ylen; y++ {
			if board[x][y] == 'X' {
				board[x][y] = '.'
				dfs(x, y)
				result++
			}
		}
	}

	return result
}

func main() {
	fmt.Println(countBattleships([][]byte{{'X', '.', '.', 'X'}, {'.', '.', '.', 'X'}, {'.', '.', '.', 'X'}, {'.', '.', '.', '.'}}))
	fmt.Println(countBattleships([][]byte{{'.'}}))
}
