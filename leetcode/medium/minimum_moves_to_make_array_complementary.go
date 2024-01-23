package main

import (
	"fmt"
)

func max(a int, b int) int {
	if a < b {
		return b
	}
	return a
}

func min(a int, b int) int {
	if a < b {
		return a
	}
	return b
}

func minMoves(nums []int, limit int) int {
	result := len(nums)

	temp := make([]int, limit*2+2)

	left, right := 0, len(nums)-1
	for i := 0; i < len(nums)/2; i++ {
		minValue := min(nums[left], nums[right]) + 1
		maxValue := max(nums[left], nums[right]) + limit

		temp[minValue] -= 1
		temp[nums[left]+nums[right]] -= 1
		temp[nums[left]+nums[right]+1] += 1
		temp[maxValue+1] += 1

		left, right = left+1, right-1
	}

	min := 100001
	for i := 1; i < len(temp); i++ {
		temp[i] += temp[i-1]
		if temp[i] < min {
			min = temp[i]
		}
	}

	return result + min
}

func main() {
	fmt.Println(minMoves([]int{1, 2, 2, 1}, 2))
	fmt.Println(minMoves([]int{1, 2, 2, 2, 4, 3}, 4))
	fmt.Println(minMoves([]int{1, 2, 4, 3}, 4))
	fmt.Println(minMoves([]int{1, 2, 1, 2}, 2))
	fmt.Println(minMoves([]int{20744, 7642, 19090, 9992, 2457, 16848, 3458, 15721}, 22891))
}

// func minMoves(nums []int, limit int) int {
// 	left, right := 0, len(nums)-1
// 	target := make(map[int]bool)
// 	numList := make([][]int, len(nums)/2)

// 	maxValue, minValue := 0, 100001

// 	for _, num := range nums {
// 		if maxValue < num {
// 			maxValue = num
// 		}

// 		if num < minValue {
// 			minValue = num
// 		}
// 	}

// 	target[maxValue+1] = true
// 	target[minValue+1] = true

// 	for i := 0; i < len(nums)/2; i++ {
// 		sum := nums[left] + nums[right]
// 		target[sum] = true
// 		numList[i] = []int{sum, max(nums[left], nums[right]), min(nums[left], nums[right])}

// 		left, right = left+1, right-1
// 	}

// 	result := 100001

// 	for num, _ := range target {
// 		temp, pass := 0, true
// 		for _, sum := range numList {
// 			if sum[0] != num {
// 				if limit*2 < num {
// 					pass = false
// 					break
// 				}

// 				if 1 <= num-sum[1] && num-sum[1] <= limit {
// 					temp += 1
// 					continue
// 				}

// 				if 1 <= num-sum[2] && num-sum[2] <= limit {
// 					temp += 1
// 					continue
// 				}

// 				temp += 2
// 			}
// 		}

// 		if pass == true && temp < result {
// 			result = temp
// 		}
// 	}

// 	return result
// }
