package main

import "fmt"

func arraySign(nums []int) int {
	n := 0

	for _, num := range nums {
		if num < 0 {
			n++
		} else if num == 0 {
			return 0
		}
	}

	if n%2 == 0 {
		return 1
	}

	return -1
}

func main() {
	fmt.Println(arraySign([]int{-1, -2, -3, -4, 3, 2, 1}))
	fmt.Println(arraySign([]int{1, 5, 0, 2, -3}))
	fmt.Println(arraySign([]int{9, 72, 34, 29, -49, -22, -77, -17, -66, -75, -44, -30, -24}))
}
