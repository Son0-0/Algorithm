package main

import "fmt"

func sortArrayByParityII(nums []int) []int {
	result := make([]int, len(nums))
	i, j := 0, 1

	for _, num := range nums {
		if num%2 == 0 {
			result[i] = num
			i += 2
		} else {
			result[j] = num
			j += 2
		}
	}

	return result
}

func main() {
	fmt.Println(sortArrayByParityII([]int{4, 2, 5, 7}))
	fmt.Println(sortArrayByParityII([]int{2, 3}))
}
