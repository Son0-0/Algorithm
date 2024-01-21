package main

import "fmt"

func smallestEquivalentString(s1 string, s2 string, baseStr string) string {
	parents := make([]int, 26)

	for i := 0; i < 26; i++ {
		parents[i] = i
	}

	var find func(int) int

	find = func(cur int) int {
		if parents[cur] != cur {
			cur = find(parents[cur])
		}

		return cur
	}

	var union func(int, int)

	union = func(x, y int) {
		xParent := find(x)
		yParent := find(y)

		if xParent < yParent {
			parents[yParent] = xParent
		} else {
			parents[xParent] = yParent
		}
	}

	for i := 0; i < len(s1); i++ {
		union(int(byte(s1[i]))-97, int(byte(s2[i]))-97)
	}

	result := []byte{}

	for _, c := range baseStr {
		result = append(result, byte(find(int(byte(c))-97)+97))
	}

	return string(result[:])
}

func main() {
	fmt.Println(smallestEquivalentString("parker", "morris", "parser"))
	fmt.Println(smallestEquivalentString("hello", "world", "hold"))
	fmt.Println(smallestEquivalentString("leetcode", "programs", "sourcecode"))
}
