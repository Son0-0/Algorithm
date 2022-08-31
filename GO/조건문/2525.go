package main

import "fmt"

func main() {
	var h, m int
	fmt.Scanf("%d %d", &h, &m)

	var add int
	fmt.Scanf("%d", &add)

	if h == 0 {
		h = 24
	}

	target := h*60 + m + add

	var ah, am int
	ah = target / 60
	am = target % 60

	if 24 <= ah {
		ah -= 24
	}

	fmt.Printf("%d %d\n", ah, am)
}
