package main

import "fmt"

func getRow(rowIndex int) []int {
	rowIndex++
	result := []int{1}
	cur := 1

	for col := 1; col < rowIndex; col++ {
		cur = cur * (rowIndex - col)
		cur = cur / col
		result = append(result, cur)
	}

	return result
}

func main() {
	result := getRow(0)

	fmt.Println(result)
}
