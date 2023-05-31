package main

import "fmt"

func strStr(haystack string, needle string) int {
	h, n := len(haystack), len(needle)

	for i := 0; i <= h-n; i++ {
		if haystack[i:i+n] == needle {
			return i
		}
	}

	return -1
}

func main() {
	fmt.Println(strStr("a", "a"))
	fmt.Println(strStr("sadbutsad", "sad"))
	fmt.Println(strStr("leetcode", "leeto"))
}
