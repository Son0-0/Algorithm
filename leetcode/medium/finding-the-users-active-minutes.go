package main

import "fmt"

func findingUsersActiveMinutes(logs [][]int, k int) []int {
	result := make([]int, k)
	users := make(map[int]map[int]bool, k)

	for _, log := range logs {
		if _, e := users[log[0]]; e {
			users[log[0]][log[1]] = true
		} else {
			users[log[0]] = make(map[int]bool)
			users[log[0]][log[1]] = true
		}
	}

	for key := range users {
		result[len(users[key])-1]++
	}

	return result
}

// func contain(slice []int, target int) bool {
// 	for _, num := range slice {
// 		if num == target {
// 			return true
// 		}
// 	}
// 	return false
// }

// func findingUsersActiveMinutes(logs [][]int, k int) []int {
// 	result := make([]int, k)

// 	users := make(map[int]int)
// 	mins := make(map[int][]int)

// 	for _, log := range logs {
// 		uid, um := log[0], log[1]

// 		if contain(mins[um], uid) {
// 			continue
// 		} else {
// 			mins[um] = append(mins[um], uid)
// 			users[uid]++
// 		}
// 	}

// 	for key := range users {
// 		result[users[key]-1]++
// 	}

// 	return result
// }

func main() {
	fmt.Println(findingUsersActiveMinutes([][]int{{0, 5}, {1, 2}, {0, 2}, {0, 5}, {1, 3}}, 5))
}
