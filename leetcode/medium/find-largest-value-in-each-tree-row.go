package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func largestValues(root *TreeNode) []int {
	result := make([]int, 0)

	var dfs func(*TreeNode, int)

	dfs = func(cur *TreeNode, level int) {
		if cur == nil {
			return
		}

		if level <= len(result) {
			if result[level-1] < cur.Val {
				result[level-1] = cur.Val
			}
		} else {
			result = append(result, cur.Val)
		}

		dfs(cur.Left, level+1)
		dfs(cur.Right, level+1)
	}

	dfs(root, 1)

	return result
}

func main() {
	fmt.Println("Hello Leetcode")
}
