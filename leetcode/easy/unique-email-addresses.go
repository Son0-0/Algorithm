package main

import (
	"fmt"
	"strings"
)

func numUniqueEmails(emails []string) int {
	emailMap := make(map[string]bool)

	for _, email := range emails {
		e := strings.Split(email, "@")
		target := strings.Join(strings.Split(strings.Split(e[0], "+")[0], "."), "") + "@" + e[1]
		emailMap[target] = true
	}

	return len(emailMap)
}

func main() {
	fmt.Println(numUniqueEmails([]string{"test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"}))
	fmt.Println(numUniqueEmails([]string{"a@leetcode.com", "b@leetcode.com", "c@leetcode.com"}))
}
