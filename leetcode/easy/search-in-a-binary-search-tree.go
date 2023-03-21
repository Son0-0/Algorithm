/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func searchBST(root *TreeNode, val int) *TreeNode {
    var result *TreeNode

    var dfs func(*TreeNode)

    dfs = func(cur *TreeNode) {
        if cur == nil {
            return
        }

        if cur.Val == val {
            result = cur
            return
        }

        dfs(cur.Left)
        dfs(cur.Right)
    }

    dfs(root)

    return result
}
