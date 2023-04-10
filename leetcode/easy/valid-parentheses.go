package main

import "fmt"

// func isValid(s string) bool {
// 	stack := []rune{}

// 	for _, c := range s {
// 		if c == '(' || c == '{' || c == '[' {
// 			stack = append(stack, c)
// 		} else {
// 			if len(stack) == 0 {
// 				return false
// 			}

// 			if c == ')' {
// 				if stack[len(stack)-1] == '(' {
// 					stack = stack[:len(stack)-1]
// 				} else {
// 					return false
// 				}
// 			} else if c == '}' {
// 				if stack[len(stack)-1] == '{' {
// 					stack = stack[:len(stack)-1]
// 				} else {
// 					return false
// 				}
// 			} else {
// 				if stack[len(stack)-1] == '[' {
// 					stack = stack[:len(stack)-1]
// 				} else {
// 					return false
// 				}
// 			}
// 		}
// 	}

// 	return len(stack) == 0
// }

func isValid(s string) bool {
	stack := make([]rune, len(s))
	var top int

	for _, c := range s {
		switch c {
		case '(', '{', '[':
			stack[top] = c
			top++
		case ')':
			if top == 0 || stack[top-1] != '(' {
				return false
			}
			top--
		case '}':
			if top == 0 || stack[top-1] != '{' {
				return false
			}
			top--
		case ']':
			if top == 0 || stack[top-1] != '[' {
				return false
			}
			top--
		}
	}

	return top == 0
}

func main() {
	fmt.Println(isValid("()"))
	fmt.Println(isValid("()[]{}"))
	fmt.Println(isValid("(]"))
	fmt.Println(isValid("["))
}
