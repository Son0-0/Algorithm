/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
var Target int

func dfs(cur *TreeNode, visited map[int]bool) bool {
	if cur == nil {
		return false
	}

	if visited[Target-cur.Val] {
		return true
	}

	visited[cur.Val] = true

	return dfs(cur.Left, visited) || dfs(cur.Right, visited)
}

func findTarget(root *TreeNode, k int) bool {
	Target = k
	return dfs(root, make(map[int]bool))
}