package main

import "fmt"

func isBoomerang(points [][]int) bool {
	x := points[0][0]
	y := points[0][1]
	xx := points[1][0]
	yy := points[1][1]
	xxx := points[2][0]
	yyy := points[2][1]

	return x*(yy-yyy)+xx*(yyy-y)+xxx*(y-yy) != 0
}

func main() {
	fmt.Println(isBoomerang([][]int{{1, 1}, {2, 3}, {3, 2}}))
	fmt.Println(isBoomerang([][]int{{1, 1}, {2, 2}, {3, 3}}))
}
