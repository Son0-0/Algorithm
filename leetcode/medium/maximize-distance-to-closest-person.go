package main

import "fmt"

func max(a, b int) int {
	if a < b {
		return b
	}
	return a
}

func maxDistToClosest(seats []int) int {
	left, distance := -1, 0

	for i := 0; i < len(seats); i++ {
		if seats[i] == 1 {
			if left == -1 {
				distance = max(distance, i)
			} else {
				distance = max(distance, (i-left)/2)
			}
			left = i
		}
	}

	return max(distance, len(seats)-left-1)
}

func main() {
	fmt.Println(maxDistToClosest([]int{1, 0, 0, 0, 1, 0, 1}) == 2)
	fmt.Println(maxDistToClosest([]int{1, 0, 0, 0}) == 3)
	fmt.Println(maxDistToClosest([]int{0, 1}) == 1)
}
