package main

import "fmt"

func divisorGame(n int) bool {
	turn := 0

	for 1 < n {
		for i := 1; i < n; i-- {
			if n%i == 0 {
				n -= i
				break
			}
		}

		turn ^= 1
	}

	if turn == 1 {
		return true
	}

	return false
}

func main() {
	fmt.Println(divisorGame(2))
	fmt.Println(divisorGame(3))
	fmt.Println(divisorGame(4))
}
