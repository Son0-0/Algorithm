package main

import "fmt"

func backspaceCompare(s string, t string) bool {
	ss, tt := "", ""

	for _, c := range s {
		if c == '#' {
			if 0 < len(ss) {
				ss = ss[:len(ss)-1]
			}
		} else {
			ss += string(c)
		}
	}

	for _, c := range t {
		if c == '#' {
			if 0 < len(tt) {
				tt = tt[:len(tt)-1]
			}
		} else {
			tt += string(c)
		}
	}

	return ss == tt
}

func main() {
	fmt.Println(backspaceCompare("a##c", "#a#c"))
}
