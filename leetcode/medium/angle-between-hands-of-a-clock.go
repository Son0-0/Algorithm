package main

import (
	"fmt"
)

func abs(a float64) float64 {
	if a < 0 {
		return -1 * a
	}
	return a
}

func min(a, b float64) float64 {
	if a < b {
		return a
	}
	return b
}

func angleClock(hour int, minutes int) float64 {
	m := float64(minutes) / 60.00 * 360.00
	h := float64(hour)*30.00 + float64(minutes)/12.00*6.00
	diff := abs(h - m)

	return min(diff, 360-diff)
}

func main() {
	fmt.Println(angleClock(12, 30))
	fmt.Println(angleClock(3, 30))
	fmt.Println(angleClock(3, 15))
}
