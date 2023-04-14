package main

import (
	"fmt"
	"strconv"
)

func getBinary(target int) string {
	result := ""

	for target > 0 {
		result += strconv.Itoa(target % 2)
		target /= 2
	}

	return result
}

func evenOddBit(n int) []int {
	result := make([]int, 2)

	for idx, c := range getBinary(n) {
		if c == '1' {
			if idx%2 == 0 {
				result[0]++
			} else {
				result[1]++
			}
		}
	}

	return result
}

func main() {
	fmt.Println(evenOddBit(17))
	fmt.Println(evenOddBit(2))
	fmt.Println(evenOddBit(8))
}
