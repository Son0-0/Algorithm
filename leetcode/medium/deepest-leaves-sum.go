package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func deepestLeavesSum(root *TreeNode) int {
	leaves := make(map[int]int)
	depth := 0

	var dfs func(*TreeNode, int)

	dfs = func(cur *TreeNode, level int) {
		if cur == nil {
			return
		}

		if cur.Left == nil && cur.Right == nil {
			leaves[level] += cur.Val
			if depth < level {
				depth = level
			}
			return
		}

		dfs(cur.Left, level+1)
		dfs(cur.Right, level+1)
	}

	dfs(root, 1)

	return leaves[depth]
}

func main() {
	one := TreeNode{
		Val: 1,
		Left: &TreeNode{
			Val:   2,
			Left:  nil,
			Right: nil,
		},
		Right: &TreeNode{
			Val:   3,
			Left:  nil,
			Right: nil,
		},
	}

	fmt.Println(deepestLeavesSum(&one))
}
