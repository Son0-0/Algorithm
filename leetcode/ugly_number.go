func isUgly(n int) bool {
	if n <= 0 {
		return false
	} else {
		num := []int{2, 3, 5}

		for _, element := range num {
			for (n % element) == 0 {
				n /= element
			}
		}

		return n == 1
	}
}