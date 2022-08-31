package main

import "fmt"

func main() {
	var a, b int
	fmt.Scanf("%d", &a)
	fmt.Scanf("%d", &b)

	if a*b < 0 {
		if a < 0 {
			fmt.Println(2)
		} else {
			fmt.Println(4)
		}
	} else {
		if a < 0 {
			fmt.Println(3)
		} else {
			fmt.Println(1)
		}
	}
}
