package main

import "fmt"

func isCovered(ranges [][]int, left int, right int) bool {
	nums := make(map[int]bool)

	for _, rgs := range ranges {
		for i := rgs[0]; i <= rgs[1]; i++ {
			nums[i] = true
		}
	}

	for i := left; i <= right; i++ {
		if _, e := nums[i]; !e {
			return false
		}
	}

	return true
}

func main() {
	fmt.Println(isCovered([][]int{{1, 2}, {3, 4}, {5, 6}}, 2, 5))
}
