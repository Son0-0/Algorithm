package main

import (
	"fmt"
	"strconv"
)

func maximumNumber(num string, change []int) string {
	result := num
	flag := false

	for i, n := range num {
		target, _ := strconv.Atoi(string(n))

		if target < change[target] {
			result = result[:i] + strconv.Itoa(change[target]) + result[i+1:]
			flag = true
		} else if flag == true && change[target] < target {
			break
		}
	}

	return result
}

func main() {
	fmt.Println(maximumNumber("132", []int{9, 8, 5, 0, 3, 6, 4, 2, 6, 8}))
	fmt.Println(maximumNumber("021", []int{9, 4, 3, 5, 7, 2, 1, 9, 0, 6}))
	fmt.Println(maximumNumber("5", []int{1, 4, 7, 5, 3, 2, 5, 6, 9, 4}))
	fmt.Println(maximumNumber("330", []int{9, 3, 6, 3, 7, 3, 1, 4, 5, 8}))
	fmt.Println(maximumNumber("334111", []int{0, 9, 2, 3, 3, 2, 5, 5, 5, 5}))
}
