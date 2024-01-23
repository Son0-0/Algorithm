package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func kthSmallest(root *TreeNode, k int) int {
	ord, result := 0, -1

	var inorder func(*TreeNode)

	inorder = func(cur *TreeNode) {
		if cur == nil {
			return
		}

		inorder(cur.Left)
		ord++
		if ord == k {
			result = cur.Val
			return
		}

		inorder(cur.Right)
	}

	inorder(root)

	return result
}

func main() {

	two := TreeNode{
		Val:   2,
		Left:  nil,
		Right: nil,
	}

	one := TreeNode{
		Val:   1,
		Left:  nil,
		Right: &two,
	}

	four := TreeNode{
		Val:   4,
		Left:  nil,
		Right: nil,
	}

	three := TreeNode{
		Val:   3,
		Left:  &one,
		Right: &four,
	}

	fmt.Println(kthSmallest(&three, 1))
}
