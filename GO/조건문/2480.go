package main

import (
	"fmt"
	"sort"
)

func main() {
	arr := make([]int, 3)
	fmt.Scanf("%d %d %d", &arr[0], &arr[1], &arr[2])
	sort.Ints(arr)

	cnt := 0
	target := arr[0]
	answer := []int{0, target}

	for i := 1; i < 3; i++ {
		if target == arr[i] {
			cnt += 1
			if answer[0] < cnt {
				answer[0] = cnt
				answer[1] = target
			}
		} else {
			cnt = 0
			target = arr[i]
		}
	}

	switch answer[0] {
	case 0:
		fmt.Println(arr[2] * 100)
	case 1:
		fmt.Println(1000 + answer[1]*100)
	case 2:
		fmt.Println(10000 + answer[1]*1000)
	}
}
