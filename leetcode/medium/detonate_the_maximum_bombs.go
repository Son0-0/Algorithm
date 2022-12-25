package main

import "fmt"

func isIn(x1 int, y1 int, x2 int, y2 int, radius int) bool {
	x := (x1 - x2) * (x1 - x2)
	y := (y1 - y2) * (y1 - y2)

	if x+y <= radius*radius {
		return true
	}
	return false
}

func maximumDetonation(bombs [][]int) int {
	result := 0

	for idx, bomb := range bombs {
		queue := [][]int{}
		queue = append(queue, bomb)

		visited := make([]int, len(bombs))
		visited[idx] = 1

		temp := 1

		for len(queue) != 0 {
			cur := queue[0]
			queue = queue[1:]

			for i, b := range bombs {
				if visited[i] == 0 && isIn(cur[0], cur[1], b[0], b[1], cur[2]) {
					temp += 1
					visited[i] = 1
					queue = append(queue, b)
				}
			}
		}

		if result < temp {
			result = temp
		}
	}

	return result
}

func main() {
	fmt.Println(maximumDetonation([][]int{{2, 1, 3}, {6, 1, 4}}))
	fmt.Println(maximumDetonation([][]int{{1, 1, 5}, {10, 10, 5}}))
	fmt.Println(maximumDetonation([][]int{{1, 2, 3}, {2, 3, 1}, {3, 4, 2}, {4, 5, 3}, {5, 6, 4}}))
}
