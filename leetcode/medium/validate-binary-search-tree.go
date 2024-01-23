package main

import (
	"fmt"
	"math"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func isValidBST(root *TreeNode) bool {
	var inorder func(*TreeNode, int, int) bool

	inorder = func(cur *TreeNode, min, max int) bool {
		if cur == nil {
			return true
		}

		if !(min < cur.Val && cur.Val < max) {
			return false
		}

		return inorder(cur.Left, min, cur.Val) && inorder(cur.Right, cur.Val, max)
	}

	return inorder(root, math.MinInt64, math.MaxInt64)
}

func main() {

	left := TreeNode{
		Val:   1,
		Left:  nil,
		Right: nil,
	}

	right := TreeNode{
		Val:   3,
		Left:  nil,
		Right: nil,
	}

	root := TreeNode{
		Val:   2,
		Left:  &left,
		Right: &right,
	}

	fmt.Println(isValidBST(&root))

	one := TreeNode{
		Val:   1,
		Left:  nil,
		Right: nil,
	}

	three := TreeNode{
		Val:   3,
		Left:  nil,
		Right: nil,
	}

	six := TreeNode{
		Val:   6,
		Left:  nil,
		Right: nil,
	}

	four := TreeNode{
		Val:   4,
		Left:  &three,
		Right: &six,
	}

	five := TreeNode{
		Val:   5,
		Left:  &one,
		Right: &four,
	}

	fmt.Println(isValidBST(&five))

	fmt.Println(isValidBST(&TreeNode{
		Val:   2147483647,
		Left:  nil,
		Right: nil,
	}))
}
