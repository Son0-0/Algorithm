package main

import "fmt"

func main() {
	var X int
	fmt.Scanf("%d", &X)

	var N int
	fmt.Scanf("%d", &N)

	answer := 0
	for i := 0; i < N; i++ {
		var a, b int
		fmt.Scanf("%d %d", &a, &b)

		answer += a * b
	}

	if answer == X {
		fmt.Println("Yes")
	} else {
		fmt.Println("No")
	}
}
