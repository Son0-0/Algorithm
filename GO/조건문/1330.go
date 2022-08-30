package main

import "fmt"

func main() {
	var a, b int
	fmt.Scanf("%d %d", &a, &b)

	if a < b {
		fmt.Println("<")
	} else if b < a {
		fmt.Println(">")
	} else {
		fmt.Println("==")
	}
}
