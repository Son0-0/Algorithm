package main

import (
	"fmt"
)

func canVisitAllRooms(rooms [][]int) bool {
	result := len(rooms) - 1

	queue := []int{}
	queue = append(queue, rooms[0]...)

	visited := make([]int, len(rooms))
	visited[0] = 1

	key := make([]int, len(rooms))
	key[0] = 1

	for _, num := range rooms[0] {
		key[num] = 1
	}

	for len(queue) != 0 {
		cur := queue[0]
		queue = queue[1:]

		if visited[cur] == 0 {
			visited[cur] = 1
			result--
			for _, num := range rooms[cur] {
				if key[num] == 0 {
					queue = append(queue, num)
					key[num] = 1
				}
			}
		}
	}

	return result == 0
}

func main() {
	fmt.Println(canVisitAllRooms([][]int{{1}, {2}, {3}, {}}))
	fmt.Println(canVisitAllRooms([][]int{{1, 3}, {3, 0, 1}, {2}, {0}}))
}
