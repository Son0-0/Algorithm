package main

import "fmt"

func findJudge(n int, trust [][]int) int {
	out, in := make(map[int]int), make(map[int]int)

	if n == 1 {
		return 1
	}

	for i := 0; i < len(trust); i++ {
		o, i := trust[i][0], trust[i][1]

		if _, exist := out[o]; exist {
			out[o] += 1
		} else {
			out[o] = 1
		}

		if _, exist := in[i]; exist {
			in[i] += 1
		} else {
			in[i] = 1
		}
	}

	for key, element := range in {
		if _, exist := out[key]; !exist && element == n-1 {
			return key
		}
	}

	return -1
}

func main() {
	fmt.Println(findJudge(1, [][]int{}))
	fmt.Println(findJudge(2, [][]int{{1, 2}}))
	fmt.Println(findJudge(3, [][]int{{1, 3}, {2, 3}}))
	fmt.Println(findJudge(3, [][]int{{1, 3}, {2, 3}, {3, 1}}))
}
