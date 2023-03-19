package main

import (
	"fmt"
	"sort"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func getAllElements(root1 *TreeNode, root2 *TreeNode) []int {
	result := []int{}

	var dfs func(*TreeNode)

	dfs = func(cur *TreeNode) {
		if cur == nil {
			return
		}

		dfs(cur.Left)
		result = append(result, cur.Val)
		dfs(cur.Right)
	}

	dfs(root1)
	dfs(root2)

	sort.Ints(result)

	return result
}

func main() {
	fmt.Println(getAllElements(&TreeNode{
		Val:   1,
		Left:  nil,
		Right: nil,
	}, &TreeNode{
		Val:   2,
		Left:  nil,
		Right: nil,
	}))
}
