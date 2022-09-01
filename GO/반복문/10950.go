package main

import "fmt"

func main() {
	var N int
	fmt.Scanf("%d", &N)

	for i := 0; i < N; i++ {
		var a, b int
		fmt.Scanf("%d %d", &a, &b)
		fmt.Println(a + b)
	}
}
