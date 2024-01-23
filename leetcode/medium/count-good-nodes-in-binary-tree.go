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

func goodNodes(root *TreeNode) int {
	result := 0

	var dfs func(*TreeNode, int)

	dfs = func(cur *TreeNode, parent int) {
		if cur == nil {
			return
		}

		if parent <= cur.Val {
			result++
		}

		parent = max(parent, cur.Val)

		dfs(cur.Left, parent)
		dfs(cur.Right, parent)
	}

	dfs(root, -10001)

	return result
}

func main() {

	four := TreeNode{
		Val:   4,
		Left:  nil,
		Right: nil,
	}

	two := TreeNode{
		Val:   2,
		Left:  nil,
		Right: nil,
	}

	three := TreeNode{
		Val:   3,
		Left:  &four,
		Right: &two,
	}

	fmt.Println(goodNodes(&TreeNode{
		Val:   3,
		Left:  &three,
		Right: nil,
	}))

	fmt.Println(goodNodes(&TreeNode{
		Val:   1,
		Left:  nil,
		Right: nil,
	}))

	fmt.Println(goodNodes(&TreeNode{
		Val:  9,
		Left: nil,
		Right: &TreeNode{
			Val:  3,
			Left: nil,
			Right: &TreeNode{
				Val:   6,
				Left:  nil,
				Right: nil,
			},
		},
	}))
}
