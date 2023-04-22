package main

import (
	"fmt"
	"math"
	"strconv"
)

func convertToBinary(target int) string {
	result := ""

	for target > 0 {
		result = strconv.Itoa(target%2) + result
		target /= 2
	}

	return result
}

func findComplement(num int) int {
	result := 0

	target := convertToBinary(num)
	mul := 0

	for i := len(target) - 1; i >= 0; i-- {
		if target[i] == '0' {
			result += int(math.Pow(2, float64(mul)))
		}
		mul++
	}

	return result
}

func main() {
	fmt.Println(findComplement(5))
	fmt.Println(findComplement(1))
	fmt.Println(findComplement(2))
}
