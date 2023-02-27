package main

import (
	"fmt"
	"math"
)

var MAX = 500*5*10000 + 1 // max weigth

func returnMinMaxValue(target []int) (int, int) {
	min, max := MAX, -1

	for _, num := range target {
		if num < min {
			min = num
		}

		if max < num {
			max = num
		}
	}

	return min, max
}

func calc(target []int, max int) int {
	cur, cnt := max, 1

	for _, w := range target {
		if cur < w {
			cnt++
			cur = max - w
		} else {
			cur -= w
		}
	}

	return cnt
}

func shipWithinDays(weights []int, days int) int {
	result := MAX

	cnt := int(math.Ceil(float64(len(weights)) / float64(days)))

	left, max := returnMinMaxValue(weights)
	right := max * cnt

	for left <= right {
		mid := (left + right) / 2

		if mid < max {
			left = mid + 1
			continue
		}

		valid := calc(weights, mid)

		if valid <= days {
			if mid < result {
				result = mid
			}
			right = mid - 1
		} else {
			left = mid + 1
		}
	}

	return result
}

func main() {
	fmt.Println(shipWithinDays([]int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 1))
	fmt.Println(shipWithinDays([]int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 5))
	fmt.Println(shipWithinDays([]int{3, 2, 2, 4, 1, 4}, 3))
	fmt.Println(shipWithinDays([]int{1, 2, 3, 1, 1}, 4))
}
