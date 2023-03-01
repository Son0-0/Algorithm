package main

import (
	"fmt"
)

func numTilePossibilities(tiles string) int {
	result := make(map[string]int)

	length := len(tiles)

	var dfs func(int, map[int]bool, string)

	dfs = func(cur int, visited map[int]bool, letters string) {
		result[letters] = 1

		for i := 0; i < length; i++ {
			if _, e := visited[i]; !e {
				visited[i] = true
				dfs(i, visited, letters+string(tiles[i]))
				delete(visited, i)
			}
		}
	}

	dfs(-1, make(map[int]bool), "")

	return len(result) - 1
}

func main() {
	fmt.Println(numTilePossibilities("AAB"))
	fmt.Println(numTilePossibilities("AAABBC"))
	fmt.Println(numTilePossibilities("V"))
}
