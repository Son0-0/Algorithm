package main

import "fmt"

// return maxValue
func max(target []int) int {
	max := -1

	for _, num := range target {
		if max < num {
			max = num
		}
	}

	return max
}

func kidsWithCandies(candies []int, extraCandies int) []bool {
	result := make([]bool, len(candies))

	max := max(candies)

	for idx, candy := range candies {
		if max <= candy+extraCandies {
			result[idx] = true
		} else {
			result[idx] = false
		}
	}

	return result
}

func main() {
	fmt.Println(kidsWithCandies([]int{2, 3, 5, 1, 3}, 3))
	fmt.Println(kidsWithCandies([]int{4, 2, 1, 1, 2}, 1))
}
