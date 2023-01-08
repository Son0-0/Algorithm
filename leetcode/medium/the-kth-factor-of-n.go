package main

import (
	"fmt"
	"math"
)

func kthFactor(n int, k int) int {
	cur := 1
	target := int(math.Sqrt(float64(n)))
	for i := 1; i <= target; i++ {
		if n%i == 0 {
			if cur == k {
				return i
			}
			cur += 1
		}
	}

	for i := target; i > 0; i-- {
		if i*i == n {
			continue
		}

		if n%i == 0 {
			if cur == k {
				return n / i
			}
			cur += 1
		}
	}

	return -1
}

func main() {
	fmt.Println(kthFactor(12, 3))
	fmt.Println(kthFactor(7, 2))
	fmt.Println(kthFactor(4, 4))
}

// O(n)
// for i := 1; i <= n; i++ {
// 	if n%i == 0 {
// 		if cur == k {
// 			return i
// 		}
// 		cur += 1
// 	}
// }
