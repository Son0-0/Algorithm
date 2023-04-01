package main

import "fmt"

func combinationSum3(k int, n int) [][]int {
	result := [][]int{}

	var dfs func(int, int, int, []int)

	dfs = func(cur, size, sum int, visited []int) {
		if size == k {
			if sum == n {
				temp := make([]int, k)
				copy(temp, visited)
				result = append(result, temp)
			}
			return
		}

		for i := cur + 1; i < 10; i++ {
			dfs(i, size+1, sum+i, append(visited, i))
		}
	}

	dfs(0, 0, 0, []int{})

	return result
}

func main() {
	fmt.Println(combinationSum3(3, 7))
}
