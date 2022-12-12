package main

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
)

var days = []int{31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31}

func arriveCalc(alice []string, bob []string) int {
	arrive := []int{}

	month, _ := strconv.Atoi(alice[0])
	day, _ := strconv.Atoi(alice[1])

	for i := 0; i < month-1; i++ {
		day += days[i]
	}

	arrive = append(arrive, day)

	month, _ = strconv.Atoi(bob[0])
	day, _ = strconv.Atoi(bob[1])

	for i := 0; i < month-1; i++ {
		day += days[i]
	}

	arrive = append(arrive, day)

	sort.Ints(arrive)

	return arrive[1]
}

func leaveCalc(alice []string, bob []string) int {
	leave := []int{}

	month, _ := strconv.Atoi(alice[0])
	day, _ := strconv.Atoi(alice[1])

	for i := 0; i < month-1; i++ {
		day += days[i]
	}

	leave = append(leave, day)

	month, _ = strconv.Atoi(bob[0])
	day, _ = strconv.Atoi(bob[1])

	for i := 0; i < month-1; i++ {
		day += days[i]
	}

	leave = append(leave, day)

	sort.Ints(leave)

	return leave[0]
}

func countDaysTogether(arriveAlice string, leaveAlice string, arriveBob string, leaveBob string) int {
	// arrive 비교
	arrive := arriveCalc(strings.Split(arriveAlice, "-"), strings.Split(arriveBob, "-"))

	// leave 비교
	leave := leaveCalc(strings.Split(leaveAlice, "-"), strings.Split(leaveBob, "-"))

	result := leave - arrive

	if result < 0 {
		return 0
	}

	return result + 1
}

func main() {
	fmt.Println(countDaysTogether("08-15", "08-18", "08-16", "08-19"))
	fmt.Println(countDaysTogether("07-12", "07-13", "07-13", "07-14"))
	fmt.Println(countDaysTogether("10-01", "10-31", "11-01", "12-31"))
}
