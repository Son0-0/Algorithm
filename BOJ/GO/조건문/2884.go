package main

import "fmt"

func main() {
	var h, m int
	fmt.Scanf("%d %d", &h, &m)
	if h == 0 {
		h = 24
	}

	target := h*60 + m - 45

	var ah, am int
	ah = target / 60
	am = target % 60

	if ah == 24 {
		ah = 0
	}

	fmt.Printf("%d %d\n", ah, am)
}
