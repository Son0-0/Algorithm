package main

import (
	"fmt"
	"sort"
)

func abs(target int) int {
	if target < 0 {
		return -target
	}
	return target
}

func minCostConnectPoints(points [][]int) int {
	result := 0
	size := len(points)

	edges := make([][]int, 0)

	for i := 0; i < size-1; i++ {
		for j := i + 1; j < size; j++ {
			distance := abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
			edges = append(edges, []int{distance, i, j})
		}
	}

	sort.SliceStable(edges, func(i, j int) bool {
		return edges[i][0] < edges[j][0]
	})

	parents := make([]int, size)

	for i := 0; i < size; i++ {
		parents[i] = i
	}

	var find func(int) int

	find = func(cur int) int {
		if parents[cur] != cur {
			cur = find(parents[cur])
		}

		return cur
	}

	cnt := 0
	for _, edge := range edges {
		if cnt == size-1 {
			break
		}

		distance, src, dest := edge[0], edge[1], edge[2]

		srcParent := find(src)
		destParent := find(dest)

		if srcParent == destParent {
			continue
		}

		if srcParent < destParent {
			parents[destParent] = srcParent
		} else if destParent < srcParent {
			parents[srcParent] = destParent
		}

		result += distance
		cnt++
	}

	return result
}

func main() {
	fmt.Println(minCostConnectPoints([][]int{{0, 0}, {2, 2}, {3, 10}, {5, 2}, {7, 0}}))
	fmt.Println(minCostConnectPoints([][]int{{3, 12}, {-2, 5}, {-4, 1}}))
}
