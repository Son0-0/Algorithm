package main

import (
	"fmt"
	"strconv"
	"strings"
)

func reformatDate(date string) string {
	month := []string{"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"}
	monthMap := make(map[string]int)

	for idx, m := range month {
		monthMap[m] = idx + 1
	}

	dateSlice := strings.Split(date, " ")

	yy := dateSlice[2]
	mm := monthMap[dateSlice[1]]
	d := ""

	for _, c := range dateSlice[0] {
		if _, e := strconv.Atoi(string(c)); e != nil {
			break
		} else {
			d += string(c)
		}
	}

	dd, _ := strconv.Atoi(d)

	return fmt.Sprintf("%s-%02d-%02d", yy, mm, dd)
}

func main() {
	fmt.Println(reformatDate("20th Oct 2052"))
	fmt.Println(reformatDate("6th Jun 2052"))
}
