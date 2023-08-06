package main

import "fmt"

func romanToInt(s string) int {
	table := make(map[byte]int)

	table['I'] = 1
	table['V'] = 5
	table['X'] = 10
	table['L'] = 50
	table['C'] = 100
	table['D'] = 500
	table['M'] = 1000

	cur := len(s) - 1
	prev := 0

	result := 0
	for cur >= 0 {
		temp := table[s[cur]]

		if prev <= temp {
			result += temp
		} else {
			result -= temp
		}

		prev = temp
		cur--
	}

	return result
}

func main() {
	fmt.Println(romanToInt("III"))
	fmt.Println(romanToInt("LVIII"))
	fmt.Println(romanToInt("MCMXCIV"))
}
