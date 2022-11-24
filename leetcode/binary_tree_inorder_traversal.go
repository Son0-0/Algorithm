/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

type Result struct {
	Val []int
}

func (result *Result) inorder(root *TreeNode) {
	if root == nil {
		return
	}

	result.inorder(root.Left)
	result.Val = append(result.Val, root.Val)
	result.inorder(root.Right)
}

func inorderTraversal(root *TreeNode) []int {
	result := Result{Val: []int{}}
	result.inorder(root)

	return result.Val
}