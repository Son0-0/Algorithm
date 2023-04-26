package main

import "fmt"

func addDigits(num int) int {
	result := num

	for 10 <= num {
		result = 0
		for num != 0 {
			result += num % 10
			num /= 10
		}

		num = result
	}

	return result
}

func main() {
	fmt.Println(addDigits(38))
	fmt.Println(addDigits(0))
	fmt.Println(addDigits(1))
}
