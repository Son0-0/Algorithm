package main

import (
	"fmt"
	"strconv"
	"strings"
)

func cellsInRange(s string) []string {
	result := make([]string, 0)

	target := strings.Split(s, ":")

	startCol := target[0][0]
	startRow, _ := strconv.Atoi(target[0][1:])

	endCol := target[1][0]
	endRow, _ := strconv.Atoi(target[1][1:])

	for i := startCol; i <= endCol; i++ {
		for j := startRow; j <= endRow; j++ {
			result = append(result, string(i)+strconv.Itoa(j))
		}
	}

	return result
}

func main() {
	fmt.Println(cellsInRange("K1:L2"))
	fmt.Println(cellsInRange("A1:F1"))
}
