package main

import "fmt"

func abs(num int) int {
	if num < 0 {
		num *= -1
	}
	return num
}

func checkDistances(s string, distance []int) bool {
	alpha := make([]int, 26)
	check := make(map[int]int)

	for i, c := range s {
		if _, e := check[int(c)-97]; e {
			alpha[int(c)-97] += i - 1
		} else {
			check[int(c)-97] = 1
			alpha[int(c)-97] = -i
		}
	}

	for v := range check {
		if alpha[v] != distance[v] {
			return false
		}
	}

	return true
}

func main() {
	fmt.Println(checkDistances("abaccb", []int{1, 3, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}))
	fmt.Println(checkDistances("aa", []int{1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}))
}
