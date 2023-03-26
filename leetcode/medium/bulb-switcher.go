package main

import "fmt"

func findSquare(n int) int {
	if n == 0 || n == 1 {
		return n
	}

	i, result := 1, 1

	for result <= n {
		i += 1
		result = i * i
	}

	return i - 1
}

func bulbSwitch(n int) int {
	return findSquare(n)
}

// func bulbSwitch(n int) int {
// 	return int(math.Sqrt(float64(n)))
// }

func main() {
	fmt.Println(bulbSwitch(3))
	fmt.Println(bulbSwitch(0))
	fmt.Println(bulbSwitch(1))
}
