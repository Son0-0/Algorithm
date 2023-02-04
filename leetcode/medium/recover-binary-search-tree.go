package main

import (
	"sort"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func recoverTree(root *TreeNode) {
	var inorder func(*TreeNode)
	nums := []int{}

	inorder = func(cur *TreeNode) {
		if cur == nil {
			return
		}

		inorder(cur.Left)
		nums = append(nums, cur.Val)
		inorder(cur.Right)
	}

	inorder(root)

	sort.Ints(nums)

	var reArrange func(*TreeNode)
	idx := 0

	reArrange = func(cur *TreeNode) {
		if cur == nil {
			return
		}

		reArrange(cur.Left)
		cur.Val = nums[idx]
		idx++
		reArrange(cur.Right)
	}

	reArrange(root)
}

func main() {
	two := TreeNode{
		Val:   2,
		Left:  nil,
		Right: nil,
	}

	three := TreeNode{
		Val:   3,
		Left:  nil,
		Right: &two,
	}

	one := TreeNode{
		Val:   1,
		Left:  &three,
		Right: nil,
	}

	recoverTree(&one)
}
