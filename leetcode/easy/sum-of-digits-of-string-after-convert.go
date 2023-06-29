package main

import (
	"fmt"
	"strconv"
)

func sum(target string) string {
	s := 0
	for _, c := range target {
		s += int(c - '0')
	}
	return strconv.Itoa(s)
}

func getLucky(s string, k int) int {

	target := ""
	for _, c := range s {
		target += strconv.Itoa(int(c) - 96)
	}

	for 0 < k {
		target = sum(target)
		k--
	}

	r, _ := strconv.Atoi(target)

	return r
}

func main() {
	fmt.Println(getLucky("leetcode", 2))
}
