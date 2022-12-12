package main

import (
	"fmt"
	"sort"
)

func longestCommonPrefix(strs []string) string {
	longestPrefix := ""

	sort.Strings(strs)

	first := string(strs[0])
	last := string(strs[len(strs)-1])

	for i := 0; i < len(first); i++ {
		if string(first[i]) == string(last[i]) {
			longestPrefix += string(last[i])
		} else {
			break
		}
	}

	return longestPrefix
}

func main() {
	fmt.Println(longestCommonPrefix([]string{"flower", "flow", "flight"}))
}
