package main

import "fmt"

var result int

func binary_search(left, right, target int) {
	if right < left {
		return
	}

	mid := (left + right) / 2

	if mid*(mid+1) <= 2*target {
		if result < mid {
			result = mid
		}
		binary_search(mid+1, right, target)
	} else {
		binary_search(left, mid-1, target)
	}
}

func arrangeCoins(n int) int {
	result = 0

	binary_search(0, n, n)

	return result
}

func main() {
	fmt.Println(arrangeCoins(5))
	fmt.Println(arrangeCoins(8))
}
