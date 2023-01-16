package main

import "fmt"

func groupThePeople(groupSizes []int) [][]int {
	result := [][]int{}
	groupMap := make(map[int][]int)

	for i, member := range groupSizes {
		groupMap[member] = append(groupMap[member], i)
	}

	for key := range groupMap {
		for i := 0; i < len(groupMap[key])/key; i++ {
			result = append(result, groupMap[key][key*i:key*(i+1)])
		}
	}

	return result
}

func main() {
	fmt.Println(groupThePeople([]int{3, 3, 3, 3, 3, 1, 3}))
	fmt.Println(groupThePeople([]int{2, 1, 3, 3, 3, 2}))
}
