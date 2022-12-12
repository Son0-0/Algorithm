package main

import "fmt"

func flipAndInvertImage(image [][]int) [][]int {
	for i := 0; i < len(image); i++ {
		length := len(image[i])

		// flip
		for j := 0; j < length/2; j++ {
			image[i][j], image[i][length-j-1] = image[i][length-j-1]^1, image[i][j]^1
		}

		// invert (XOR)
		half := length / 2
		if length%2 != 0 {
			image[i][half] ^= 1
		}
	}

	return image
}

func main() {
	fmt.Println(flipAndInvertImage([][]int{{1, 1, 0}, {1, 0, 1}, {0, 0, 0}}))
	fmt.Println(flipAndInvertImage([][]int{{1, 1, 0, 0}, {1, 0, 0, 1}, {0, 1, 1, 1}, {1, 0, 1, 0}}))
}
