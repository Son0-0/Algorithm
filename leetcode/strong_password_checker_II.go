package main

import (
	"fmt"
	"strings"
	"unicode"
)

func strongPasswordCheckerII(password string) bool {
	if len(password) < 8 {
		return false
	}

	var lower, upper, special, digit bool
	prev := ""

	for _, str := range password {
		if prev == string(str) {
			return false
		}
		prev = string(str)

		if unicode.IsDigit(str) {
			digit = true
		}

		if 65 <= str && str <= 90 {
			upper = true
		} else if 97 <= str && str <= 122 {
			lower = true
		}

		if strings.Contains("!@#$%^&*()-+", string(str)) {
			special = true
		}
	}

	if lower && upper && digit && special {
		return true
	}

	return false
}

func main() {
	fmt.Println(strongPasswordCheckerII("IloveLe3tcode!"))
	fmt.Println(strongPasswordCheckerII("Me+You--IsMyDream"))
	fmt.Println(strongPasswordCheckerII("1aB!"))
	fmt.Println(strongPasswordCheckerII("11A!A!Aa"))
}
