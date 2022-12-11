package main

import (
	"fmt"
	"sort"
)

func findContentChildren(g []int, s []int) int {
	sort.Ints(g)
	sort.Ints(s)

	result := 0

	for _, cookie := range s {
		if g[result] <= cookie {
			result += 1
		}

		if result == len(g) {
			return result
		}
	}

	return result
}

func main() {
	fmt.Println(findContentChildren([]int{1, 2, 3}, []int{1, 1}))
	fmt.Println(findContentChildren([]int{1, 2}, []int{1, 2, 3}))
	fmt.Println(findContentChildren([]int{1, 2, 3}, []int{3}))
}

