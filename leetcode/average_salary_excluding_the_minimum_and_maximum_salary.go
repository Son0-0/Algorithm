package main

import (
	"fmt"
	"math"
)

func average(salary []int) float64 {
	min, max := math.Inf(1), math.Inf(-1)
	var sum float64 = 0

	for _, s := range salary {
		s := float64(s)
		sum += s

		if s < min {
			min = s
		}

		if max < s {
			max = s
		}
	}

	return (sum - min - max) / float64((len(salary) - 2))
}

func main() {
	fmt.Println(average([]int{4000, 3000, 1000, 2000}))
	fmt.Println(average([]int{1000, 2000, 3000}))
}
