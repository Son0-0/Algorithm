package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func pruneTree(root *TreeNode) *TreeNode {
	var dfs func(*TreeNode) bool

	dfs = func(cur *TreeNode) bool {
		if cur == nil {
			return true
		}

		left, right := dfs(cur.Left), dfs(cur.Right)

		if left {
			cur.Left = nil
		}

		if right {
			cur.Right = nil
		}

		return left && right && cur.Val == 0
	}

	if dfs(root) {
		return nil
	}

	return root
}

func main() {
	three := TreeNode{
		Val:   0,
		Left:  nil,
		Right: nil,
	}

	four := TreeNode{
		Val:   1,
		Left:  nil,
		Right: nil,
	}

	two := TreeNode{
		Val:   0,
		Left:  &three,
		Right: &four,
	}

	one := TreeNode{
		Val:   1,
		Left:  nil,
		Right: &two,
	}

	var inorder func(*TreeNode)

	inorder = func(cur *TreeNode) {
		if cur == nil {
			return
		}

		fmt.Println(cur.Val)
		inorder(cur.Left)
		inorder(cur.Right)
	}

	inorder(&one)

	fmt.Println("====")

	pruneTree(&one)

	inorder(&one)
}
