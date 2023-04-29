package main

import "fmt"

func validPath(n int, edges [][]int, source int, destination int) bool {
	parents := make([]int, n)

	for i := 0; i < n; i++ {
		parents[i] = i
	}

	// find function for finding current node's parents
	var find func(int) int

	find = func(cur int) int {
		if parents[cur] != cur {
			parents[cur] = find(parents[cur])
		}

		return parents[cur]
	}

	// union function for union two nodes
	var union func(int, int)

	union = func(x, y int) {
		xParents := find(x)
		yParents := find(y)

		if xParents < yParents {
			parents[yParents] = xParents
		} else {
			parents[xParents] = yParents
		}
	}

	for _, edge := range edges {
		union(edge[0], edge[1])
	}

	return find(source) == find(destination)
}

func main() {
	fmt.Println(validPath(3, [][]int{{0, 1}, {1, 2}, {2, 0}}, 0, 2))
}
