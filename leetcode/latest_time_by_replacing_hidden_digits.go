package main

import (
	"fmt"
)

func maximumTime(time string) string {
	nums := []byte("0123456789?")

	for i := 0; i < 5; i++ {
		target := string(time[i])

		if string(time[i]) == "?" {
			if i == 0 {
				if nums[4] <= byte(time[1]) && byte(time[1]) < nums[10] {
					target = "1"
				} else {
					target = "2"
				}
			} else if i == 1 {
				if nums[2] <= byte(time[0]) {
					target = "3"
				} else {
					target = "9"
				}
			} else if i == 3 {
				target = "5"
			} else if i == 4 {
				target = "9"
			}
		}

		time = time[:i] + target + time[i+1:]
	}

	return time
}

func main() {
	fmt.Println(maximumTime("2?:?0"))
	fmt.Println(maximumTime("0?:3?"))
	fmt.Println(maximumTime("1?:22"))
	fmt.Println(maximumTime("??:3?"))
}
