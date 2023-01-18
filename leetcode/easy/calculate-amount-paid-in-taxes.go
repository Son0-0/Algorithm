package main

import "fmt"

func calculateTax(brackets [][]int, income int) float64 {
	curIncome := 0

	if brackets[0][0] <= income {
		curIncome = brackets[0][0]
	} else {
		return float64(income*brackets[0][1]) / 100
	}

	result := float64(curIncome*brackets[0][1]) / 100

	for i := 1; i < len(brackets); i++ {
		target := brackets[i][0] - brackets[i-1][0]

		if curIncome+target <= income {
			result += float64(target*brackets[i][1]) / 100
		} else {
			result += float64((income-curIncome)*brackets[i][1]) / 100
			break
		}

		curIncome += target
	}

	return result
}

func main() {
	fmt.Println(calculateTax([][]int{{3, 50}, {7, 10}, {12, 25}}, 10))
	fmt.Println(calculateTax([][]int{{1, 0}, {4, 25}, {5, 50}}, 2))
	fmt.Println(calculateTax([][]int{{2, 50}}, 0))
}
