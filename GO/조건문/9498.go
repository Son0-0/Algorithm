package main

import "fmt"

func main() {
	var score int
	fmt.Scanf("%d", &score)

	score /= 10

	switch score {
	case 10:
		fmt.Println("A")
	case 9:
		fmt.Println("A")
	case 8:
		fmt.Println("B")
	case 7:
		fmt.Println("C")
	case 6:
		fmt.Println("D")
	default:
		fmt.Println("F")
	}
}
