package main

import "fmt"

func decode(encoded []int, first int) []int {
	result := []int{first}

	cur := first
	for _, num := range encoded {
		result = append(result, cur^num)
		cur ^= num
	}

	return result
}

func main() {
	fmt.Println(decode([]int{1, 2, 3}, 1))
	fmt.Println(decode([]int{6, 2, 7, 3}, 4))
}
