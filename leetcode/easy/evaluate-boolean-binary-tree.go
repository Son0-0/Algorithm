package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func evaluateTree(root *TreeNode) bool {
	var postorder func(*TreeNode) int

	postorder = func(node *TreeNode) int {
		if node == nil {
			return 0
		}

		left := postorder(node.Left)
		right := postorder(node.Right)

		if node.Val == 2 {
			return left | right
		} else if node.Val == 3 {
			return left & right
		} else {
			return node.Val
		}
	}

	if postorder(root) == 1 {
		return true
	}

	return false
}

func main() {

	t1 := TreeNode{
		Val:   1,
		Left:  nil,
		Right: nil,
	}

	f1 := TreeNode{
		Val:   0,
		Left:  nil,
		Right: nil,
	}

	t2 := TreeNode{
		Val:   1,
		Left:  nil,
		Right: nil,
	}

	a1 := TreeNode{
		Val:   3,
		Left:  &f1,
		Right: &t2,
	}

	o1 := TreeNode{
		Val:   2,
		Left:  &t1,
		Right: &a1,
	}

	fmt.Println(evaluateTree(&o1))

	fmt.Println(evaluateTree(&f1))
}
