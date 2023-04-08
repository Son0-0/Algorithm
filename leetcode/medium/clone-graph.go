package main

import "fmt"

type Node struct {
	Val       int
	Neighbors []*Node
}

func cloneGraph(node *Node) *Node {
	if node == nil {
		return nil
	}

	first := node.Val
	nInfo := make(map[int][]int)
	nodeMap := make(map[int]*Node)

	var helper func(*Node)

	helper = func(cur *Node) {
		if cur == nil {
			return
		}

		nodeMap[cur.Val] = &Node{
			Val:       cur.Val,
			Neighbors: make([]*Node, 0),
		}

		nInfo[cur.Val] = make([]int, len(cur.Neighbors))

		for i, n := range cur.Neighbors {
			nInfo[cur.Val][i] = n.Val
			if _, e := nodeMap[n.Val]; !e {
				helper(n)
			}
		}
	}

	helper(node)

	for key := range nInfo {
		for _, v := range nInfo[key] {
			nodeMap[key].Neighbors = append(nodeMap[key].Neighbors, nodeMap[v])
		}
	}

	return nodeMap[first]
}

func main() {
	one := Node{
		Val:       1,
		Neighbors: make([]*Node, 0),
	}

	two := Node{
		Val:       2,
		Neighbors: make([]*Node, 0),
	}

	three := Node{
		Val:       3,
		Neighbors: make([]*Node, 0),
	}

	four := Node{
		Val:       4,
		Neighbors: make([]*Node, 0),
	}

	one.Neighbors = append(one.Neighbors, &two)
	one.Neighbors = append(one.Neighbors, &four)

	two.Neighbors = append(two.Neighbors, &one)
	two.Neighbors = append(two.Neighbors, &three)

	three.Neighbors = append(three.Neighbors, &two)
	three.Neighbors = append(three.Neighbors, &four)

	four.Neighbors = append(four.Neighbors, &one)
	four.Neighbors = append(four.Neighbors, &three)

	fmt.Println(cloneGraph(&one))

	fmt.Println(cloneGraph(&Node{
		Val:       1,
		Neighbors: []*Node{},
	}))

	fmt.Println(cloneGraph(nil))
}
