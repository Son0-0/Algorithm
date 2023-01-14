package main

import "fmt"

func max(a, b int) int {
	if a < b {
		return b
	}
	return a
}

func maxDistance(colors []int) int {
	// result := 0

	left, right := 0, len(colors)-1

	for colors[0] == colors[right] {
		right -= 1
	}

	for colors[len(colors)-1] == colors[left] {
		left += 1
	}

	return max(right, len(colors)-left-1)

	/*
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
	*/
}

func main() {
	fmt.Println(maxDistance([]int{1, 1, 1, 6, 1, 1, 1}))
	fmt.Println(maxDistance([]int{1, 8, 3, 8, 3}))
}
