package main

import (
	"fmt"
	"sort"
)

func minimumOperations(nums []int) int {

	target := make(map[int]int)

	total := 0
	for _, num := range nums {
		if num != 0 {
			target[num] = num
		}
		total += num
	}

	sub := []int{}
	for num := range target {
		sub = append(sub, num)
	}

	sort.Ints(sub)

	sum := 0
	cnt := 0

	for total != 0 {
		temp := sub[cnt] - sum
		for i := 0; i < len(nums); i++ {
			if nums[i] != 0 {
				nums[i] -= temp
				total -= temp
			}
		}
		sum += temp
		cnt += 1
	}

	return cnt
}

func main() {
	fmt.Println(minimumOperations([]int{1, 5, 0, 3, 5}))
	fmt.Println(minimumOperations([]int{0}))
}
