package main

import "fmt"

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

func longestZigZag(root *TreeNode) int {

	var dfs func(*TreeNode, int, int) int

	dfs = func(cur *TreeNode, rightOrLeft, length int) int {
		if cur == nil {
			return length
		}

		length++

		left, right := 0, 0

		switch rightOrLeft {
		// right case
		case 0:
			left = dfs(cur.Left, 1, length)
			right = max(dfs(cur.Right, 0, 0), length)

		// left case
		case 1:
			left = max(dfs(cur.Left, 1, 0), length)
			right = dfs(cur.Right, 0, length)
		}

		return max(left, right)
	}

	return max(dfs(root.Right, 0, 0), dfs(root.Left, 1, 0))
}

func main() {
	// root := TreeNode {
	// 	Val: 1,
	// 	Left: ,
	// }

	third := TreeNode{
		Val:   1,
		Left:  nil,
		Right: nil,
	}

	second := TreeNode{
		Val:   1,
		Left:  nil,
		Right: &third,
	}

	root := TreeNode{
		Val:   1,
		Left:  &second,
		Right: nil,
	}

	fmt.Println(longestZigZag(&root))
}
