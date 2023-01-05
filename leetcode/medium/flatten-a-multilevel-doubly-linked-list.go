package main

import "fmt"

type Node struct {
	Val   int
	Prev  *Node
	Next  *Node
	Child *Node
}

func flatten(root *Node) *Node {
	nodes := []*Node{}

	if root == nil {
		return nil
	}

	var dfs func(*Node)

	dfs = func(node *Node) {
		nodes = append(nodes, node)

		if node.Child != nil {
			dfs(node.Child)
		}

		if node.Next != nil {
			dfs(node.Next)
		}
	}

	dfs(root)

	for i := 0; i < len(nodes); i++ {
		if i == len(nodes)-1 {
			nodes[i].Next = nil
			nodes[i].Prev = nodes[i-1]
		} else {
			nodes[i].Next = nodes[i+1]
			if i == 0 {
				nodes[i].Prev = nil
			} else {
				nodes[i].Prev = nodes[i-1]
			}
		}
		nodes[i].Child = nil
	}

	return nodes[0]
}

func main() {
	two := Node{
		Val:   2,
		Prev:  nil,
		Next:  nil,
		Child: nil,
	}

	three := Node{
		Val:   3,
		Prev:  nil,
		Next:  nil,
		Child: nil,
	}

	one := Node{
		Val:   1,
		Next:  &two,
		Prev:  nil,
		Child: &three,
	}

	two.Prev = &one

	temp := flatten(&one)

	for {
		if temp == nil {
			break
		}

		fmt.Println(temp.Val)
		temp = temp.Next
	}
}
