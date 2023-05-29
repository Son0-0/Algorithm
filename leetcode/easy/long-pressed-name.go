package main

import "fmt"

func isLongPressedName(name string, typed string) bool {
	n, t := 0, 0

	for n <= len(name) && t < len(typed) {
		if n < len(name) && name[n] == typed[t] {
			n++
			t++
		} else if t != 0 && typed[t-1] == typed[t] {
			t++
		} else {
			return false
		}
	}

	return n == len(name) && t == len(typed)
}

func main() {
	fmt.Println(isLongPressedName("alex", "aaleex"))
	fmt.Println(isLongPressedName("alex", "aaleexa"))
	fmt.Println(isLongPressedName("saeed", "ssaaedd"))
}
