/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func preorderTraversal(root *TreeNode) []int {
	result := []int{}

	var preorder func(*TreeNode)

	preorder = func(cur *TreeNode) {
		if cur == nil {
			return
		}

		result = append(result, cur.Val)
		preorder(cur.Left)
		preorder(cur.Right)
	}

	preorder(root)

	return result
}
