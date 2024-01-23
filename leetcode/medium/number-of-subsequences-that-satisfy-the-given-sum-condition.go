package main

import "fmt"

func numSubseq(nums []int, target int) int {
	MOD := 1000000007
	
	size := len(nums)-1
	cnt := 0
	
	pow := make([]int, len(nums))
	pow[0] = 1

	for i := 1; i <= size; i++ {
		pow[i] = (pow[i-1] * 2) % MOD
	}

	sort.Ints(nums)

	for l, r := 0, size; l <= r; {
		if nums[l] + nums[r] <= target {
			cnt = (cnt + pow[r-l]) % MOD
			l++
		} else {
			r--
		}
	}


	return cnt
}

func main() {
	fmt.Println(numSubseq([]int{3,5,6,7}, 9))
	fmt.Println(numSubseq([]int{3,3,6,8}, 10))
}