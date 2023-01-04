package main

import "fmt"

func maximumXOR(nums []int) int {
	result := 0

	for _, num := range nums {
		result |= num
	}

	return result
}

func main() {
	fmt.Println(maximumXOR([]int{3, 2, 4, 6}))
	fmt.Println(maximumXOR([]int{1, 2, 3, 9, 2}))
}
