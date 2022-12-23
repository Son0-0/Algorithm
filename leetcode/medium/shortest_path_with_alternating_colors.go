package main

import "fmt"

func shortestAlternatingPaths(n int, redEdges [][]int, blueEdges [][]int) []int {
	result := []int{}
	for i := 0; i < n; i++ {
		result = append(result, 101)
	}
	result[0] = 0

	redGraph, blueGraph := make([][]int, n), make([][]int, n)

	for _, edge := range redEdges {
		s, d := edge[0], edge[1]
		redGraph[s] = append(redGraph[s], d)
	}

	for _, edge := range blueEdges {
		s, d := edge[0], edge[1]
		blueGraph[s] = append(blueGraph[s], d)
	}

	queue := [][]int{}

	for _, node := range redGraph[0] {
		queue = append(queue, []int{node, 1, 0})
		if node != 0 {
			result[node] = 1
		}
	}

	for _, node := range blueGraph[0] {
		queue = append(queue, []int{node, 1, 1})
		if node != 0 {
			result[node] = 1
		}
	}

	for len(queue) != 0 {
		cur := queue[0] // cur[0] = current node, cur[1] = current distance, cur[2] = current color
		queue = queue[1:]

		// if color is red
		if cur[2] == 0 {
			for idx, node := range blueGraph[cur[0]] {
				if node != -1 {
					queue = append(queue, []int{node, cur[1] + 1, 1})
					if cur[1]+1 < result[node] {
						result[node] = cur[1] + 1
					}

					blueGraph[cur[0]][idx] = -1
				}
			}
		} else { // if color is blue
			for idx, node := range redGraph[cur[0]] {
				if node != -1 {
					queue = append(queue, []int{node, cur[1] + 1, 0})
					if cur[1]+1 < result[node] {
						result[node] = cur[1] + 1
					}

					redGraph[cur[0]][idx] = -1
				}
			}
		}
	}

	for idx, num := range result {
		if num == 101 {
			result[idx] = -1
		}
	}

	return result
}

func main() {
	fmt.Println(shortestAlternatingPaths(5, [][]int{{0, 1}, {1, 2}, {2, 3}, {3, 4}}, [][]int{{1, 2}, {2, 3}, {3, 1}}))
	// fmt.Println(shortestAlternatingPaths(3, [][]int{{0, 1}, {0, 2}}, [][]int{{1, 0}}))
	// fmt.Println(shortestAlternatingPaths(3, [][]int{{0, 1}}, [][]int{{1, 2}}))
	// fmt.Println(shortestAlternatingPaths(3, [][]int{{0, 1}, {1, 2}}, [][]int{}))
	// fmt.Println(shortestAlternatingPaths(3, [][]int{{0, 1}}, [][]int{{2, 1}}))
}
