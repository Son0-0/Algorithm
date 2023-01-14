package main

import "fmt"

func maxDistance(colors []int) int {
	result := 0

	for i := 0; i < len(colors)-1; i++ {
		for j := i + 1; j < len(colors); j++ {
			if colors[i] != colors[j] {
				if result < j-i {
					result = j - i
				}
			}
		}
	}

	return result
}

func main() {
	fmt.Println(maxDistance([]int{1, 1, 1, 6, 1, 1, 1}))
	fmt.Println(maxDistance([]int{1, 8, 3, 8, 3}))
}
