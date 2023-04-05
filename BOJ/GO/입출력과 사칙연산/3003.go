package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	chessOfBlack := []int{1, 1, 2, 2, 2, 8}

	var input string
	reader := bufio.NewReader(os.Stdin)
	input, _ = reader.ReadString('\n')
	input = strings.TrimSpace(input)

	chess := strings.Split(input, " ")

	for i, str := range chess {
		target, _ := strconv.Atoi(str)
		fmt.Print(chessOfBlack[i]-target, " ")
	}
}
