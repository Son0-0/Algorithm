package main

import "fmt"

func numEquivDominoPairs(dominoes [][]int) int {
	result, nums := 0, make([][]int, 10)

	for i := 0; i < 10; i++ {
		nums[i] = make([]int, 10)
	}

	for _, d := range dominoes {
		begin, end := d[0], d[1]

		result += nums[begin][end]

		if begin != end {
			result += nums[end][begin]
		}

		nums[begin][end]++
	}

	return result
}

func main() {
	fmt.Println(numEquivDominoPairs([][]int{{1, 2}, {2, 1}, {3, 4}, {5, 6}}))
}
