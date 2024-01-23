package main

import "fmt"

func findOrder(numCourses int, prerequisites [][]int) []int {
	graph := make(map[int][]int)
	preqMap := make(map[int]int)

	for i := 0; i < numCourses; i++ {
		preqMap[i] = 0
	}

	for _, p := range prerequisites {
		preqMap[p[0]]++
		graph[p[1]] = append(graph[p[1]], p[0])
	}

	queue := []int{}

	for key, val := range preqMap {
		if val == 0 {
			queue = append(queue, key)
		}
	}

	result := []int{}
	for len(queue) != 0 {
		// popleft
		cur := queue[0]
		queue = queue[1:]

		result = append(result, cur)

		if len(result) == numCourses {
			return result
		}

		for _, val := range graph[cur] {
			preqMap[val]--
			if preqMap[val] == 0 {
				queue = append(queue, val)
			}

		}
	}

	return []int{}
}

func main() {
	fmt.Println(findOrder(2, [][]int{{1, 0}}))
	fmt.Println(findOrder(4, [][]int{{1, 0}, {2, 0}, {3, 1}, {3, 2}}))
	fmt.Println(findOrder(2, [][]int{}))
	fmt.Println(findOrder(2, [][]int{{0, 1}}))
	fmt.Println(findOrder(1, [][]int{}))
}
