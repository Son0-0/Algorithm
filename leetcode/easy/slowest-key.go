package main

import "fmt"

func slowestKey(releaseTimes []int, keysPressed string) byte {
	maxDuration := 0
	var maxAlpha byte
	cur := 0

	for idx, time := range releaseTimes {
		if maxDuration < time-cur {
			maxDuration = time - cur
			maxAlpha = keysPressed[idx]
		} else if maxDuration == time-cur {
			if maxAlpha < keysPressed[idx] {
				maxAlpha = keysPressed[idx]
			}
		}
		cur = time
	}

	return maxAlpha
}

func main() {
	fmt.Println(slowestKey([]int{9, 29, 49, 50}, "cbcd"))
	fmt.Println(slowestKey([]int{12, 23, 36, 46, 62}, "spuda"))
}
