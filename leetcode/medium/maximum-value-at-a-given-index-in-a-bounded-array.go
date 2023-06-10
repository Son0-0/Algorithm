package main

import "fmt"

func max(a, b int) int {
	if a < b {
		return b
	}
	return a
}

func sum(target int) int {
	if target <= 0 {
		return 0
	}
	return (target * (target + 1)) / 2
}

func maxValue(n int, index int, maxSum int) int {
	result := 0

	left, right := 1, maxSum

	var validate func(int) bool

	validate = func(mid int) bool {
		leftSum, rightSum := 0, 0

		if mid-1 < index {
			leftSum += index - mid + 1
		}

		if index != 0 {
			leftSum += sum(mid-1) - sum(mid-1-index)
		}

		if mid < n-index {
			rightSum += n - index - mid
		}

		if index != n-1 {
			rightSum += sum(mid-1) - sum(mid-n+index)
		}

		return (leftSum + mid + rightSum) <= maxSum
	}

	for left <= right {
		mid := (left + right) / 2

		if validate(mid) == true {
			left = mid + 1
			result = max(result, mid)
		} else {
			right = mid - 1
		}
	}

	return result
}

func main() {
	fmt.Println(maxValue(4, 2, 6))
	fmt.Println(maxValue(6, 1, 10))
	fmt.Println(maxValue(3, 2, 18))
	fmt.Println(maxValue(8, 7, 14))
	fmt.Println(maxValue(4, 3, 4))
	fmt.Println(maxValue(8, 6, 20))
}
