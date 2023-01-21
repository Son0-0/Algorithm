package main

import "fmt"

func totalMoney(n int) int {
	if n <= 7 {
		return (n * (n + 1)) / 2
	}

	temp := 28
	a, b := n/7, n%7

	return temp*a + 7*(a*(a-1))/2 + (b*(b+1))/2 + b*a
}

func main() {
	fmt.Println(totalMoney(21))
	fmt.Println(totalMoney(4))
	fmt.Println(totalMoney(10))
	fmt.Println(totalMoney(20))
}
