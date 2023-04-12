package main

import (
	"fmt"
	"strings"
)

func simplifyPath(path string) string {
	stack := make([]string, len(path))
	top := 0

	for _, dir := range strings.Split(path, "/") {
		switch dir {
		case "":
			continue
		case ".":
			continue
		case "..":
			if 0 < top {
				top--
			}
		default:
			stack[top] = dir
			top++
		}
	}

	return "/" + strings.Join(stack[:top], "/")
}

func main() {
	fmt.Println(simplifyPath("/home/"))
	fmt.Println(simplifyPath("/../"))
	fmt.Println(simplifyPath("/home//foo/"))
}
