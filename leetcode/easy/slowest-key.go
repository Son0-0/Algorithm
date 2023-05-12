package main

import "fmt"

func slowestKey(releaseTimes []int, keysPressed string) byte {
	maxDuration := 0
	var maxAlpha byte
	cur := 0

	for idx, time := range releaseTimes {
		fmt.Println(time - cur)
		if maxDuration < time-cur {
			maxDuration = time - cur
			if maxAlpha < keysPressed[idx] {
				maxAlpha = keysPressed[idx]
			}
		}
		cur = time
	}

	return maxAlpha
}

func main() {
	fmt.Println(slowestKey([]int{12, 23, 36, 46, 62}, "spuda"))
}
