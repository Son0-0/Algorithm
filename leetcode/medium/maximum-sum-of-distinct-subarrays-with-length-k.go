package main

import "fmt"

func max(a, b int64) int64 {
	if a < b {
		return b
	}
	return a
}

func isValid(target map[int]int) bool {
	for _, value := range target {
		if value > 1 {
			return false
		}
	}
	return true
}

func maximumSubarraySum(nums []int, k int) int64 {
	var result int64

	if len(nums) < k {
		return result
	}

	curMap := make(map[int]int)
	flag := true
	var curSum int64
	for i := 0; i < k; i++ {
		curSum += int64(nums[i])

		if _, e := curMap[nums[i]]; e {
			flag = false
		}
		curMap[nums[i]]++
	}

	if flag {
		result = max(result, curSum)
	}

	for i := 1; i < len(nums)-k+1; i++ {
		curSum = curSum - int64(nums[i-1]) + int64(nums[i+k-1])

		// left element
		curMap[nums[i-1]]--
		if curMap[nums[i-1]] == 0 {
			delete(curMap, nums[i-1])
		} else if curMap[nums[i-1]] > 1 {
			flag = false
		}

		// right element
		curMap[nums[i+k-1]]++
		if curMap[nums[i+k-1]] > 1 {
			flag = false
		}

		if flag == false {
			if isValid(curMap) {
				flag = true
			}
		}

		if flag == true {
			result = max(result, curSum)
		}
	}

	return int64(result)
}

func main() {
	fmt.Println(maximumSubarraySum([]int{1, 1, 1, 7, 8, 9}, 3))
	fmt.Println(maximumSubarraySum([]int{1, 5, 4, 2, 9, 9, 9}, 3))
	fmt.Println(maximumSubarraySum([]int{4, 4, 4}, 3))
}
