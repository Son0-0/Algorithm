package main

import (
	"fmt"
	"strconv"
)

func convertToBase7(num int) string {
	minus, result := "", ""

	if num == 0 {
		return "0"
	} else if num < 0 {
		minus = "-"
		num *= -1
	}

	for 0 < num {
		result = strconv.Itoa(num%7) + result
		num /= 7
	}

	return minus + result
}

func main() {
	fmt.Println(convertToBase7(100))
	fmt.Println(convertToBase7(-7))
	fmt.Println(convertToBase7(7))
}
