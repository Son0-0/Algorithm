package main

import "fmt"

func main() {

	// N := 101
	var N int
	fmt.Scanf("%d", &N)

	a := make([][]int, N)
	for i := range a {
		a[i] = make([]int, 10)
	}

	fmt.Println(a)
}
