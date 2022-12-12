package main

import "fmt"

func mostVisited(n int, rounds []int) []int {
	result := []int{}

	start, end := rounds[0], rounds[len(rounds)-1]

	if start <= end {
		for i := start; i <= end; i++ {
			result = append(result, i)
		}
	} else {
		for i := 1; i <= end; i++ {
			result = append(result, i)
		}

		for i := start; i <= n; i++ {
			result = append(result, i)
		}
	}

	return result
}

func main() {
	fmt.Println(mostVisited(4, []int{1, 4, 1}))
	fmt.Println(mostVisited(4, []int{1, 3, 1, 2}))
	fmt.Println(mostVisited(2, []int{2, 1, 2, 1, 2, 1, 2, 1, 2}))
	fmt.Println(mostVisited(7, []int{1, 3, 5, 7}))
}
