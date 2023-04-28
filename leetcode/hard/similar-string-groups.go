package main

import (
	"fmt"
)

func check(a, b string) bool {
	if a == b {
		return true
	}

	i, size := 0, len(a)
	comp := 0

	for i != size {
		if a[i] != b[i] {
			comp++
		}

		if 2 < comp {
			return false
		}

		i++
	}

	return comp == 2
}

func numSimilarGroups(strs []string) int {
	size := len(strs)
	graph := make([][]int, size)

	var dfs func(int, []int)

	dfs = func(cur int, visited []int) {
		if len(visited) == 2 {
			if check(strs[visited[0]], strs[visited[1]]) {
				graph[visited[0]] = append(graph[visited[0]], visited[1])
				graph[visited[1]] = append(graph[visited[1]], visited[0])
			}
			return
		}

		for i := cur + 1; i < size; i++ {
			dfs(i, append(visited, i))
		}
	}

	dfs(-1, []int{})

	visited := make([]bool, size)
	result := 0

	var dfs2 func(int)

	dfs2 = func(cur int) {
		visited[cur] = true
		for _, node := range graph[cur] {
			if !visited[node] {
				dfs2(node)
			}
		}
	}

	for i := 0; i < size; i++ {
		if !visited[i] {
			result++
			dfs2(i)
		}
	}

	return result
}

func main() {
	fmt.Println(numSimilarGroups([]string{"tars", "rats", "arts", "star"}))
	fmt.Println(numSimilarGroups([]string{"omv", "ovm"}))
	fmt.Println(numSimilarGroups([]string{"blw", "bwl", "wlb"}))
	fmt.Println(numSimilarGroups([]string{"abc", "abc"}))
	fmt.Println(numSimilarGroups([]string{"kccomwcgcs", "socgcmcwkc", "sgckwcmcoc", "coswcmcgkc", "cowkccmsgc", "cosgmccwkc", "sgmkwcccoc", "coswmccgkc", "kowcccmsgc", "kgcomwcccs"}))
	fmt.Println(numSimilarGroups([]string{"ajdidocuyh", "djdyaohuic", "ddjyhuicoa", "djdhaoyuic", "ddjoiuycha", "ddhoiuycja", "ajdydocuih", "ddjiouycha", "ajdydohuic", "ddjyouicha"}))
	fmt.Println(numSimilarGroups([]string{"qihcochwmglyiggvsqqfgjjxu", "gcgqxiysqfqugmjgwclhjhovi", "gjhoggxvcqlcsyifmqgqujwhi", "wqoijxciuqlyghcvjhgsqfmgg", "qshcoghwmglygqgviiqfjcjxu", "jgcxqfqhuyimjglgihvcqsgow", "qshcoghwmggylqgviiqfjcjxu", "wcoijxqiuqlyghcvjhgsqgmgf", "qshcoghwmglyiqgvigqfjcjxu", "qgsjggjuiyihlqcxfovchqmwg", "wcoijxjiuqlyghcvqhgsqgmgf", "sijgumvhqwqioclcggxgyhfjq", "lhogcgfqqihjuqsyicxgwmvgj", "ijhoggxvcqlcsygfmqgqujwhi", "qshcojhwmglyiqgvigqfgcjxu", "wcoijxqiuqlyghcvjhgsqfmgg", "qshcojhwmglyiggviqqfgcjxu", "lhogcgqqfihjuqsyicxgwmvgj", "xscjjyfiuglqigmgqwqghcvho", "lhggcgfqqihjuqsyicxgwmvoj", "lhgocgfqqihjuqsyicxgwmvgj", "qihcojhwmglyiggvsqqfgcjxu", "ojjycmqshgglwicfqguxvihgq", "sijvumghqwqioclcggxgyhfjq", "gglhhifwvqgqcoyumcgjjisqx"}))
}
