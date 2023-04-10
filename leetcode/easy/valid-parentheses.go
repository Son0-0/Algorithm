package main

import "fmt"

func isValid(s string) bool {
	stack := []rune{}

	for _, c := range s {
		if c == '(' || c == '{' || c == '[' {
			stack = append(stack, c)
		} else {
			if len(stack) == 0 {
				return false
			}

			if c == ')' {
				if stack[len(stack)-1] == '(' {
					stack = stack[:len(stack)-1]
				} else {
					return false
				}
			} else if c == '}' {
				if stack[len(stack)-1] == '{' {
					stack = stack[:len(stack)-1]
				} else {
					return false
				}
			} else {
				if stack[len(stack)-1] == '[' {
					stack = stack[:len(stack)-1]
				} else {
					return false
				}
			}
		}
	}

	return len(stack) == 0
}

func main() {
	fmt.Println(isValid("()"))
	fmt.Println(isValid("()[]{}"))
	fmt.Println(isValid("(]"))
}
