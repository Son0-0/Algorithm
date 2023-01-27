package main

import "fmt"

func isPowerOfFour(n int) bool {
	for 0 < n && n%4 == 0 {
		n /= 4
	}

	return n == 1
}

func main() {
	fmt.Println(isPowerOfFour(16))
	fmt.Println(isPowerOfFour(5))
	fmt.Println(isPowerOfFour(1))
}
