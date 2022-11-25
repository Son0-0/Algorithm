package main

import "fmt"

func convertToTitle(columnNumber int) string {
	alphabet := "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

	result := ""

	for 0 < columnNumber {
		result = string(alphabet[(columnNumber-1)%26]) + result
		columnNumber = (columnNumber - 1) / 26
	}

	return result
}

func main() {
	fmt.Println(convertToTitle(52))
	fmt.Println(convertToTitle(26))
	fmt.Println(convertToTitle(1))
	fmt.Println(convertToTitle(28))
	fmt.Println(convertToTitle(701))
	fmt.Println(convertToTitle(727))
}
