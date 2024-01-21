package main

import (
	"fmt"
	"math"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func max(a, b int) int {
	if a < b {
		return b
	}
	return a
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func widthOfBinaryTree(root *TreeNode) int {
	result := 0
	nums := make(map[int][]int)

	var inorder func(*TreeNode, int, int)

	inorder = func(cur *TreeNode, level, curVal int) {
		if cur == nil {
			return
		}

		if _, e := nums[level]; !e {
			nums[level] = append(nums[level], []int{-math.MaxInt, math.MaxInt}...)
		}

		// [max, min]
		nums[level][0] = max(nums[level][0], curVal)
		nums[level][1] = min(nums[level][1], curVal)

		if nums[level][0] != -math.MaxInt && nums[level][1] != math.MaxInt {
			result = max(result, nums[level][0]-nums[level][1]+1)
		}

		inorder(cur.Left, level+1, curVal*2)
		inorder(cur.Right, level+1, curVal*2+1)
	}

	inorder(root, 0, 1)

	return result
}

func main() {
	five := TreeNode{
		Val:   5,
		Left:  nil,
		Right: nil,
	}

	three2 := TreeNode{
		Val:   3,
		Left:  nil,
		Right: nil,
	}

	nine := TreeNode{
		Val:   9,
		Left:  nil,
		Right: nil,
	}

	two := TreeNode{
		Val:   2,
		Left:  nil,
		Right: &nine,
	}

	three1 := TreeNode{
		Val:   3,
		Left:  &five,
		Right: &three2,
	}

	root := TreeNode{
		Left:  &three1,
		Right: &two,
	}

	fmt.Println(widthOfBinaryTree(&root))
}
