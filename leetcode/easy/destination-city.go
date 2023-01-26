package main

import "fmt"

func destCity(paths [][]string) string {
	city := make(map[string]bool)
	graph := make(map[string][]string)

	for _, path := range paths {
		city[path[0]], city[path[1]] = true, true
		graph[path[0]] = append(graph[path[0]], path[1])
	}

	for key := range city {
		if _, e := graph[key]; !e {
			return key
		}
	}

	return ""
}

func main() {
	fmt.Println(destCity([][]string{{"London", "New York"}, {"New York", "Lima"}, {"Lima", "Sao Paulo"}}))
	fmt.Println(destCity([][]string{{"B", "C"}, {"D", "B"}, {"C", "A"}}))
	fmt.Println(destCity([][]string{{"A", "Z"}}))
}
