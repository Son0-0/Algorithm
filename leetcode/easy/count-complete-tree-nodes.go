package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func countNodes(root *TreeNode) int {
	count := 0

	if root == nil {
		return count
	}

	var inorder func(*TreeNode)

	inorder = func(cur *TreeNode) {
		if cur == nil {
			return
		}

		inorder(cur.Left)
		count++
		inorder(cur.Right)
	}

	inorder(root)

	return count
}

func main() {
	four := TreeNode{
		Val:   4,
		Left:  nil,
		Right: nil,
	}

	five := TreeNode{
		Val:   5,
		Left:  nil,
		Right: nil,
	}

	six := TreeNode{
		Val:   6,
		Left:  nil,
		Right: nil,
	}

	two := TreeNode{
		Val:   2,
		Left:  &four,
		Right: &five,
	}

	three := TreeNode{
		Val:   3,
		Left:  &six,
		Right: nil,
	}

	one := TreeNode{
		Val:   1,
		Left:  &two,
		Right: &three,
	}

	fmt.Println(countNodes(&one))
}
