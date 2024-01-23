package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

var (
	result int
	depth  int
)

func inorder(node *TreeNode, cur int) {
	if node == nil {
		return
	}

	inorder(node.Left, cur+1)
	if depth < cur {
		depth = cur
		result = node.Val
	}
	inorder(node.Right, cur+1)
}

func findBottomLeftValue(root *TreeNode) int {
	depth = -1

	inorder(root, 0)

	return result
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

	tree := TreeNode{
		Val:   2,
		Left:  &left,
		Right: &right,
	}

	fmt.Println(findBottomLeftValue(&tree))

	left = TreeNode{
		Val:   -1,
		Left:  nil,
		Right: nil,
	}

	tree = TreeNode{
		Val:   0,
		Left:  &left,
		Right: nil,
	}

	fmt.Println(findBottomLeftValue(&tree))
}
