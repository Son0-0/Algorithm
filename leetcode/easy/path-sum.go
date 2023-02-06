package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func hasPathSum(root *TreeNode, targetSum int) bool {
	result := false

	if root == nil {
		return result
	}

	var inorder func(*TreeNode, int)

	inorder = func(cur *TreeNode, sum int) {
		if cur == nil {
			return
		}

		if sum+cur.Val == targetSum {
			if cur.Left == nil && cur.Right == nil {
				result = true
			}
		}

		inorder(cur.Left, sum+cur.Val)
		inorder(cur.Right, sum+cur.Val)
	}

	inorder(root, 0)

	return result
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
		Right: nil,
	}

	one := TreeNode{
		Val:   1,
		Left:  &two,
		Right: &three,
	}

	fmt.Println(hasPathSum(&one, 3))
	fmt.Println(hasPathSum(nil, 0))
}
