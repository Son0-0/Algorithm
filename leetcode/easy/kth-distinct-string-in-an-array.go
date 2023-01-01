package main

import "fmt"

func kthDistinct(arr []string, k int) string {
	distinct := make(map[string]int)
	order := []string{}

	for _, str := range arr {
		target := string(str)
		if _, exists := distinct[target]; exists {
			distinct[target] += 1
		} else {
			distinct[target] = 1
			order = append(order, string(str))
		}
	}

	cnt := 0
	for _, str := range order {
		if distinct[str] == 1 {
			cnt += 1
		}

		if cnt == k {
			return str
		}
	}

	return ""
}

func main() {
	fmt.Println(kthDistinct([]string{"d", "b", "c", "b", "c", "a"}, 2))
	fmt.Println(kthDistinct([]string{"aaa", "aa", "a"}, 1))
	fmt.Println(kthDistinct([]string{"a", "b", "a"}, 3))
}
