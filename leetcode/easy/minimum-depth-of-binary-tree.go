package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func minDepth(root *TreeNode) int {
	result := 100001

	var dfs func(*TreeNode, int)

	dfs = func(cur *TreeNode, depth int) {
		if cur == nil {
			return
		}

		if cur.Left == nil && cur.Right == nil {
			if depth < result {
				result = depth
			}
			return
		}

		dfs(cur.Left, depth+1)
		dfs(cur.Right, depth+1)
	}

	dfs(root, 1)

	if result == 100001 {
		return 0
	}

	return result
}

func main() {
	of := TreeNode{
		Val:   15,
		Left:  nil,
		Right: nil,
	}

	sv := TreeNode{
		Val:   7,
		Left:  nil,
		Right: nil,
	}

	tt := TreeNode{
		Val:   20,
		Left:  &of,
		Right: &sv,
	}

	ne := TreeNode{
		Val:   9,
		Left:  nil,
		Right: nil,
	}

	root := TreeNode{
		Val:   3,
		Left:  &ne,
		Right: &tt,
	}

	fmt.Println(minDepth(&root))
}
