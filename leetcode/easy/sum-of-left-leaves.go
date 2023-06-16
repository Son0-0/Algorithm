package main

import "fmt"

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func sumOfLeftLeaves(root *TreeNode) int {
	result := 0

	var inorder func(*TreeNode, string)

	inorder = func(cur *TreeNode, dir string) {
		if cur == nil {
			return
		}

		if dir == "L" {
			if cur.Left == nil && cur.Right == nil {
				result += cur.Val
			}
		}

		inorder(cur.Left, "L")
		inorder(cur.Right, "R")
	}

	inorder(root, "R")

	return result
}

func main() {
	nine := TreeNode{
		Val:   9,
		Left:  nil,
		Right: nil,
	}

	ft := TreeNode{
		Val:   15,
		Left:  nil,
		Right: nil,
	}

	seven := TreeNode{
		Val:   7,
		Left:  nil,
		Right: nil,
	}

	tw := TreeNode{
		Val:   20,
		Left:  &ft,
		Right: &seven,
	}

	fmt.Println(sumOfLeftLeaves(&TreeNode{
		Val:   3,
		Left:  &nine,
		Right: &tw,
	}))
}
