package main

import (
	"fmt"
	"sort"
)

func sortEvenOdd(nums []int) []int {
	oddNums, evenNums := make([]int, 0), make([]int, 0)
	result := make([]int, len(nums))

	for i, num := range nums {
		if i%2 == 0 {
			evenNums = append(evenNums, num)
		} else {
			oddNums = append(oddNums, num)
		}
	}

	sort.Ints(evenNums)
	sort.Slice(oddNums, func(i, j int) bool {
		return oddNums[i] > oddNums[j]
	})

	odd, even := 1, 0
	for _, num := range evenNums {
		result[even] = num
		even += 2
	}

	for _, num := range oddNums {
		result[odd] = num
		odd += 2
	}

	return result
}

func main() {
	fmt.Println(sortEvenOdd([]int{4, 1, 2, 3}))
}
