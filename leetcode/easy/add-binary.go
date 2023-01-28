package main

import (
	"fmt"
	"strconv"
)

func addBinary(a string, b string) string {
	result, carry := "", 0

	ai, bi := len(a)-1, len(b)-1

	for 0 <= ai || 0 <= bi || carry == 1 {
		if 0 <= ai {
			c, _ := strconv.Atoi(string(a[ai]))
			carry += c
		}

		if 0 <= bi {
			c, _ := strconv.Atoi(string(b[bi]))
			carry += c
		}

		result = strconv.Itoa(carry%2) + result
		carry /= 2

		ai--
		bi--
	}

	return result
}

func main() {
	fmt.Println(addBinary("11", "1"))
	fmt.Println(addBinary("1010", "1011"))
}
