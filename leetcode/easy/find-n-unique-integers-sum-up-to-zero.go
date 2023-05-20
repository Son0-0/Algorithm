package main

import "fmt"

func sumZero(n int) []int {

	if n == 1 {
		return []int{0}
	}

	result := []int{}

	if n%2 == 1 {
		for i := 1; i <= n/2; i++ {
			result = append(result, []int{i, -i}...)
		}
		result = append(result, 0)
	} else {
		for i := 1; i <= n/2; i++ {
			result = append(result, []int{i, -i}...)
		}
	}

	return result
}

func main() {
	fmt.Println(sumZero(5))
	fmt.Println(sumZero(3))
	fmt.Println(sumZero(1))
	fmt.Println(sumZero(4))
}
