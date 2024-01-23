package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func averageOfSubtree(root *TreeNode) int {
	var dfs func(*TreeNode) (int, int, int)

	dfs = func(cur *TreeNode) (int, int, int) {
		if cur == nil {
			return 0, 0, 0
		}

		left, lcnt, lnum := dfs(cur.Left)
		right, rcnt, rnum := dfs(cur.Right)

		csum := left + right + cur.Val
		ccnt := lcnt + rcnt + 1
		cnum := lnum + rnum

		if csum/ccnt == cur.Val {
			cnum++
		}

		return csum, ccnt, cnum
	}

	_, _, result := dfs(root)

	return result
}

func main() {

	fmt.Println(averageOfSubtree(&TreeNode{
		Val:   1,
		Left:  nil,
		Right: nil,
	}))

}
