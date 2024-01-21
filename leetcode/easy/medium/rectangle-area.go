package main

import "fmt"

func max(a, b int) int {
	if a < b {
		return b
	}
	return a
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func computeArea(ax1 int, ay1 int, ax2 int, ay2 int, bx1 int, by1 int, bx2 int, by2 int) int {
	result := (ax2-ax1)*(ay2-ay1) + (bx2-bx1)*(by2-by1)

	a, b, c, d := max(ax1, bx1), min(ax2, bx2), max(ay1, by1), min(ay2, by2)

	if b <= a {
		return result
	} else if d <= c {
		return result
	}

	return result - (b-a)*(d-c)
}

func main() {
	fmt.Println(computeArea(-3, 0, 3, 4, 0, -1, 9, 2))
	fmt.Println(computeArea(-2, -2, 2, 2, -2, -2, 2, 2))
	fmt.Println(computeArea(-2, -2, 2, 2, -1, 4, 1, 6))
}
