package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func isSameTree(p *TreeNode, q *TreeNode) bool {
	result := true

	var inorder func(*TreeNode, *TreeNode)

	inorder = func(pc, qc *TreeNode) {
		if pc == nil && qc == nil {
			return
		} else if pc == nil && qc != nil {
			result = false
			return
		} else if pc != nil && qc == nil {
			result = false
			return
		}

		if pc.Val != qc.Val {
			result = false
			return
		}

		inorder(pc.Left, qc.Left)
		inorder(pc.Right, qc.Right)
	}

	inorder(p, q)

	return result
}

func main() {

	two := TreeNode{
		Val:   2,
		Left:  nil,
		Right: nil,
	}

	two2 := TreeNode{
		Val:   2,
		Left:  nil,
		Right: nil,
	}

	three := TreeNode{
		Val:   3,
		Left:  nil,
		Right: nil,
	}

	three2 := TreeNode{
		Val:   3,
		Left:  nil,
		Right: nil,
	}

	one := TreeNode{
		Val:   1,
		Left:  &two,
		Right: &three,
	}

	one2 := TreeNode{
		Val:   1,
		Left:  &two2,
		Right: &three2,
	}

	fmt.Println(isSameTree(&one, &one2))
}
