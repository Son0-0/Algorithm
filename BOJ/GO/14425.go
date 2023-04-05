package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	br = bufio.NewReader(os.Stdin)
	bw = bufio.NewWriter(os.Stdout)
)

func main() {
	defer bw.Flush()

	var n, m int
	fmt.Fscanln(br, &n, &m)

	str := make(map[string]int)
	for i := 0; i < n; i++ {
		s, _ := br.ReadString('\n')
		str[s] = 1
	}

	answer := 0
	for i := 0; i < m; i++ {
		s, _ := br.ReadString('\n')
		if str[s] != 0 {
			answer++
		}
	}

	fmt.Fprint(bw, answer)
}
