package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func postorderTraversal(root *TreeNode) []int {
	result := []int{}

	var postorder func(*TreeNode)

	postorder = func(cur *TreeNode) {
		if cur == nil {
			return
		}

		postorder(cur.Left)
		postorder(cur.Right)

		result = append(result, cur.Val)
	}

	postorder(root)

	return result
}

func main() {
	fmt.Println(postorderTraversal(&TreeNode{
		Val:   1,
		Left:  nil,
		Right: nil,
	}))
}
