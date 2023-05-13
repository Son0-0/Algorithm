package main

import "fmt"

func isToeplitzMatrix(matrix [][]int) bool {
	row := make([]int, len(matrix[0]))
	copy(row, matrix[0])

	for i := 1; i < len(matrix); i++ {
		for j := 1; j < len(matrix[i]); j++ {
			if matrix[i][j] != row[j-1] {
				return false
			}
		}
		copy(row, matrix[i])
	}

	return true
}

func main() {
	fmt.Println(isToeplitzMatrix([][]int{{1, 2, 3, 4}, {5, 1, 2, 3}, {9, 5, 1, 2}}))
}
