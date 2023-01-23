package main

import "fmt"

func findNumbers(nums []int) int {
	result := 0

	for _, num := range nums {
		if num == 100000 {
			result++
			continue
		}

		for _, t := range []int{100, 10000} {
			target := num % t
			if target == num {
				if 10 <= target && target < 100 {
					result++
					break
				} else if 1000 <= target && target < 10000 {
					result++
					break
				}
			}
		}
	}

	return result
}

func main() {
	fmt.Println(findNumbers([]int{12, 345, 2, 6, 7896}))
	fmt.Println(findNumbers([]int{555, 901, 482, 1771}))
}
