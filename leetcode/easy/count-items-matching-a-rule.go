package main

import "fmt"

func countMatches(items [][]string, ruleKey string, ruleValue string) int {

	idx := 0
	itemMap := make(map[string]int)

	if ruleKey == "color" {
		idx = 1
	}

	for _, item := range items {
		itemMap[item[idx]]++
	}

	return itemMap[ruleValue]
}

func main() {
	fmt.Println(countMatches([][]string{{"phone", "blue", "pixel"}, {"computer", "silver", "lenovo"}, {"phone", "gold", "iphone"}}, "color", "silver"))
	fmt.Println(countMatches([][]string{{"phone", "blue", "pixel"}, {"computer", "silver", "lenovo"}, {"phone", "gold", "iphone"}}, "type", "phone"))
}
