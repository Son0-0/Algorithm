package main

func findSquare(n int) int {
	if n == 0 || n == 1 {
		return n
	}

	i, result := 1, 1

	for result <= n {
		i += 1
		result = i * i
	}

	return i - 1
}

func bulbSwitch(n int) int {
	return findSquare(n)
}
