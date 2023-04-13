package main

import "fmt"

func validateStackSequences(pushed []int, popped []int) bool {
	stack := make([]int, len(pushed))
	top, ptr := -1, 0

	for _, num := range pushed {
		if num == popped[ptr] {
			ptr++
		} else {
			for top != -1 && stack[top] == popped[ptr] {
				ptr++
				top--
			}

			top++
			stack[top] = num
		}
	}

	for 0 <= top {
		if stack[top] != popped[ptr] {
			return false
		} else {
			top--
			ptr++
		}
	}

	return true
}

// func validateStackSequences(pushed []int, popped []int) bool {
// 	stack := []int{}
// 	ptr := 0

// 	for _, num := range pushed {
// 		if num == popped[ptr] {
// 			ptr++
// 		} else {
// 			for len(stack) != 0 && stack[len(stack)-1] == popped[ptr] {
// 				ptr++
// 				stack = stack[:len(stack)-1]
// 			}
// 			stack = append(stack, num)
// 		}
// 	}

// 	if len(stack) != len(popped[ptr:]) {
// 		return false
// 	}

// 	size := len(popped)
// 	for ptr < size {
// 		if stack[len(stack)-1] != popped[ptr] {
// 			return false
// 		} else {
// 			ptr++
// 			stack = stack[:len(stack)-1]
// 		}
// 	}

// 	return true
// }

func main() {
	fmt.Println(validateStackSequences([]int{1, 2, 3, 4, 5}, []int{4, 5, 3, 2, 1}))
	fmt.Println(validateStackSequences([]int{1, 2, 3, 4, 5}, []int{4, 3, 5, 1, 2}))
	fmt.Println(validateStackSequences([]int{2, 1, 0}, []int{1, 2, 0}))
	fmt.Println(validateStackSequences([]int{2, 3, 0, 1}, []int{0, 3, 2, 1}))
}
