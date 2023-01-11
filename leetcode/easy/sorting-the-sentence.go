package main

import (
	"fmt"
	"strconv"
	"strings"
)

func sortSentence(s string) string {
	order := make(map[int]string)

	for _, str := range strings.Split(s, " ") {
		index, _ := strconv.Atoi(string(str[len(str)-1]))
		order[index] = str[:len(str)-1]
	}

	result := ""
	for idx := 1; idx <= len(order); idx++ {
		result += order[idx] + " "
	}

	return result[:len(result)-1]
}

func main() {
	fmt.Println(sortSentence("is2 sentence4 This1 a3"))
	fmt.Println(sortSentence("Myself2 Me1 I4 and3"))
}
