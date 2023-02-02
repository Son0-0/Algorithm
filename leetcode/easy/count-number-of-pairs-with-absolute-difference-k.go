package main

import "fmt"

// * HASHMAP
func countKDifference(nums []int, k int) int {
	numMap := make(map[int]int)

	for _, num := range nums {
		numMap[num]++
	}

	result := 0
	for key := range numMap {
		if _, e := numMap[key+k]; e {
			result += numMap[key] * numMap[key+k]
		}
	}

	return result
}

// * DFS (brute force)
// func abs(target int) int {
// 	if target < 0 {
// 		return -target
// 	}
// 	return target
// }

// func countKDifference(nums []int, k int) int {
// 	result := 0

// 	var dfs func(int, []int)

// 	dfs = func(cur int, visited []int) {
// 		if len(visited) == 2 {
// 			if abs(nums[visited[0]]-nums[visited[1]]) == k {
// 				result++
// 			}
// 			return
// 		}

// 		for i := cur + 1; i < len(nums); i++ {
// 			dfs(i, append(visited, i))
// 		}
// 	}

// 	dfs(-1, []int{})

// 	return result
// }

func main() {
	fmt.Println(countKDifference([]int{1, 2, 2, 1}, 1))
	fmt.Println(countKDifference([]int{1, 3}, 3))
	fmt.Println(countKDifference([]int{3, 2, 1, 5, 4}, 2))
}
