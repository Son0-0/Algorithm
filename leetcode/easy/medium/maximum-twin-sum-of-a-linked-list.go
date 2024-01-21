package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func max(a, b int) int {
	if a < b {
		return b
	}
	return a
}

func pairSum(head *ListNode) int {
	result := 0

	nums := []int{}
	length := 0

	for head != nil {
		nums = append(nums, head.Val)
		head = head.Next
		length++
	}

	for i := 0; i < length/2; i++ {
		result = max(result, nums[i]+nums[length-i-1])
	}

	return result
}

func main() {

	one := ListNode{
		Val:  1,
		Next: nil,
	}

	two := ListNode{
		Val:  2,
		Next: &one,
	}

	four := ListNode{
		Val:  4,
		Next: &two,
	}

	root := ListNode{
		Val:  5,
		Next: &four,
	}

	fmt.Println(pairSum(&root))

}
