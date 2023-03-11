package main

func moveZeroes(nums []int) {
	pos := 0
	for idx, num := range nums {
		if num != 0 {
			nums[pos], nums[idx] = nums[idx], nums[pos]
			pos++
		}
	}
}

func main() {
	moveZeroes([]int{0, 1, 0, 3, 12})
}
