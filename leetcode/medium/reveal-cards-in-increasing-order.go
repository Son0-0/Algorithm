package main

import (
	"fmt"
	"sort"
)

func deckRevealedIncreasing(deck []int) []int {
	result := []int{}

	sort.SliceStable(deck, func(a, b int) bool {
		return deck[a] > deck[b]
	})

	for _, num := range deck {
		if len(result) != 0 {
			result = append([]int{result[len(result)-1]}, result[:len(result)-1]...)
		}
		result = append([]int{num}, result...)
	}

	return result
}

func main() {
	fmt.Println(deckRevealedIncreasing([]int{17, 13, 11, 2, 3, 5, 7}))
	fmt.Println(deckRevealedIncreasing([]int{1, 1000}))
}
