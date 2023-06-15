package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func maxLevelSum(root *TreeNode) int {
	levels := make(map[int]int)

	var inorder func(*TreeNode, int)

	inorder = func(cur *TreeNode, level int) {
		if cur == nil {
			return
		}

		inorder(cur.Left, level+1)
		levels[level] += cur.Val
		inorder(cur.Right, level+1)
	}

	inorder(root, 1)

	level, result := 1, levels[1]

	for key := range levels {
		if result < levels[key] {
			result = levels[key]
			level = key
		}
	}

	return level
}

func main() {
	seven1 := TreeNode{
		Val:   7,
		Left:  nil,
		Right: nil,
	}

	eight := TreeNode{
		Val:   -8,
		Left:  nil,
		Right: nil,
	}

	seven2 := TreeNode{
		Val:   7,
		Left:  &seven1,
		Right: &eight,
	}

	zero := TreeNode{
		Val:   0,
		Left:  nil,
		Right: nil,
	}

	root := TreeNode{
		Val:   1,
		Left:  &seven2,
		Right: &zero,
	}

	fmt.Println(maxLevelSum(&root))
}
