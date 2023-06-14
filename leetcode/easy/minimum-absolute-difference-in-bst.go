package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func abs(target int) int {
	if target < 0 {
		return -target
	}
	return target
}

func getMinimumDifference(root *TreeNode) int {
	prev, result := -100001, 100001

	var inorder func(*TreeNode)

	inorder = func(cur *TreeNode) {
		if cur == nil {
			return
		}

		inorder(cur.Left)
		result = min(result, abs(cur.Val-prev))
		prev = cur.Val
		inorder(cur.Right)
	}

	inorder(root)

	return result
}

func main() {
	one := TreeNode{
		Val:   1,
		Left:  nil,
		Right: nil,
	}

	three := TreeNode{
		Val:   3,
		Left:  nil,
		Right: nil,
	}

	two := TreeNode{
		Val:   2,
		Left:  &one,
		Right: &three,
	}

	six := TreeNode{
		Val:   6,
		Left:  nil,
		Right: nil,
	}

	four := TreeNode{
		Val:   4,
		Left:  &two,
		Right: &six,
	}

	fmt.Println(getMinimumDifference(&four))
}
