package main

import "fmt"

func waysToMakeFair(nums []int) int {
	result := 0

	oddSum, evenSum := 0, 0
	oddCur, evenCur := 0, 0

	for index, num := range nums {
		if index%2 == 0 {
			evenSum += num
		} else {
			oddSum += num
		}
	}

	for index, num := range nums {
		if index%2 == 0 {
			evenSum -= num
			if (evenSum + oddCur) == (oddSum + evenCur) {
				result++
			}
			evenCur += num
		} else {
			oddSum -= num
			if (evenSum + oddCur) == (oddSum + evenCur) {
				result++
			}
			oddCur += num
		}
	}

	return result
}

func main() {
	fmt.Println(waysToMakeFair([]int{2, 1, 6, 4}))
	fmt.Println(waysToMakeFair([]int{1, 1, 1}))
	fmt.Println(waysToMakeFair([]int{1, 2, 3}))
}
