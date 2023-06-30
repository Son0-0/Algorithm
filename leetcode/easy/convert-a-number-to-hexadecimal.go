package main

import "fmt"

func toHex(num int) string {
	hex := "0123456789abcdef"

	if num == 0 {
		return "0"
	} else if num < 0 {
		num = -num
		num ^= 0xffffffff
		num += 1
	}

	result := ""

	for 0 < num {
		digit := num % 16
		result = string(hex[digit]) + result
		num /= 16
	}

	return result
}

func main() {
	fmt.Println(toHex(26))
	fmt.Println(toHex(-1))
}
