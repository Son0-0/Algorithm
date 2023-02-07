package main

import (
	"fmt"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func pathSum(root *TreeNode, targetSum int) [][]int {
	result := [][]int{}

	if root == nil {
		return result
	}

	var inorder func(*TreeNode, int, []int)

	inorder = func(cur *TreeNode, sum int, visited []int) {
		if cur == nil {
			return
		}

		if sum+cur.Val == targetSum {
			if cur.Left == nil && cur.Right == nil {
				temp := make([]int, len(visited)+1)
				copy(temp, append(visited, cur.Val))
				result = append(result, temp)
				return
			}
		}

		inorder(cur.Left, sum+cur.Val, append(visited, cur.Val))
		inorder(cur.Right, sum+cur.Val, append(visited, cur.Val))
	}

	inorder(root, 0, []int{})

	return result
}

func main() {
	two := TreeNode{
		Val:   2,
		Left:  nil,
		Right: nil,
	}

	three := TreeNode{
		Val:   3,
		Left:  nil,
		Right: nil,
	}

	one := TreeNode{
		Val:   1,
		Left:  &two,
		Right: &three,
	}

	fmt.Println(pathSum(&one, 3))

	one.Right = nil

	fmt.Println(pathSum(&one, 0))
}
