package main

import "fmt"

func diagonalSum(mat [][]int) int {
	result := 0
	size := len(mat)

	if size%2 == 1 {
		target := size / 2
		result -= mat[target][target]
	}

	for i := 0; i < size; i++ {
		result += mat[i][size-i-1] + mat[i][i]
	}

	return result
}

func main() {
	fmt.Println(diagonalSum([][]int{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}))
	fmt.Println(diagonalSum([][]int{{1, 1, 1, 1}, {1, 1, 1, 1}, {1, 1, 1, 1}, {1, 1, 1, 1}}))
}
