package main

import (
	"fmt"
	"strconv"
)

func minFlips(a int, b int, c int) int {
	result := 0

	bitA := strconv.FormatInt(int64(a), 2)
	lenA := len(bitA)

	bitB := strconv.FormatInt(int64(b), 2)
	lenB := len(bitB)

	bitDiff := strconv.FormatInt(int64(int64(a|b)^int64(c)), 2)
	lenD := len(bitDiff)

	bitTarget := strconv.FormatInt(int64(c), 2)
	lenT := len(bitTarget)

	for i := 0; i < len(bitDiff); i++ {
		if bitDiff[lenD-1-i] == '1' {
			if 0 <= (lenT-1-i) && bitTarget[lenT-1-i] == '1' {
				// case 1.
				result += 1
			} else {
				// case 2.
				result += 2

				aa, bb := byte('0'), byte('0')

				if i < lenA {
					aa = bitA[lenA-1-i]
				}

				if i < lenB {
					bb = bitB[lenB-1-i]
				}

				if aa != bb {
					result--
				}
			}
		}
	}

	return result
}

func main() {
	fmt.Println(minFlips(2, 6, 5))
	fmt.Println(minFlips(4, 2, 7))
	fmt.Println(minFlips(1, 2, 3))
	fmt.Println(minFlips(8, 3, 5))
}
