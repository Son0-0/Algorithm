package main

func removeDigit(number string, digit byte) string {
	result := ""

	for i := 0; i < len(number); i++ {
		if number[i] != digit {
			continue
		}

		temp := number[:i] + number[i+1:]
		if temp > result {
			result = temp
		}
	}

	return result
}
