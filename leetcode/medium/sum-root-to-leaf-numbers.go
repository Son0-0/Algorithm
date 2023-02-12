package main

import (
	"fmt"
	"strconv"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func sumNumbers(root *TreeNode) int {
	result := 0

	var dfs func(*TreeNode, string)

	dfs = func(cur *TreeNode, sum string) {
		if cur == nil {
			return
		}

		if cur.Left == nil && cur.Right == nil {
			target, _ := strconv.Atoi(sum + strconv.Itoa(cur.Val))
			result += target
		}

		dfs(cur.Left, sum+strconv.Itoa(cur.Val))
		dfs(cur.Right, sum+strconv.Itoa(cur.Val))
	}

	dfs(root, "")

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

	fmt.Println(sumNumbers(&one))
}
