package main

import "fmt"

func mySqrt(x int) int {
	left := 1
	right := x
	mid := 0

	for left <= right {
		mid = int((left + right) / 2)

		if (mid * mid) < x {
			left = mid + 1
		} else if x < (mid * mid) {
			right = mid - 1
		} else if (mid * mid) == x {
			return mid
		}
	}

	return right
}

func main() {
	fmt.Println(mySqrt(4))
	fmt.Println(mySqrt(8))
}
