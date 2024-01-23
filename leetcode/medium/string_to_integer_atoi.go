package main

import (
	"fmt"
	"math"
)

func myAtoi(s string) int {
	var result int64
	negative, cont := 1, true

	max := int64(math.Pow(2, 31) - 1)
	min := -1 * (max + 1)

	for _, c := range s {
		if cont {
			if string(c) == " " {
				continue
			} else if string(c) == "-" {
				negative = -1
				cont = false
			} else if string(c) == "+" {
				negative = 1
				cont = false
			} else if "0" <= string(c) && string(c) <= "9" {
				result += int64(rune(c) - 48)
				cont = false
			} else {
				return 0
			}
		} else {
			if "0" <= string(c) && string(c) <= "9" {
				result = result*10 + int64(rune(c)-48)
				if max < result*int64(negative) {
					return int(max)
				} else if result*int64(negative) < min {
					return int(min)
				}
			} else {
				break
			}
		}
	}

	return int(result) * negative
}

func main() {
	fmt.Println(myAtoi("9223372036854775808"))
	fmt.Println(myAtoi("2147483648"))
	fmt.Println(myAtoi("42"))
	fmt.Println(myAtoi("           -42"))
	fmt.Println(myAtoi("4193 with words"))
}
