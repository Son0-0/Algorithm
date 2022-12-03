func numDifferentIntegers(word string) int {
    word += "a"
    result := ""
    nums := make(map[string]int)
    returnValue := 0
    for _, w := range word {
        if unicode.IsDigit(w) {
            if result == "0" {
                result = string(w)
            } else {
                result += string(w)
            }
        } else {
            if len(result) != 0 {
                if _, exist := nums[result]; !exist {
                    nums[result] = 1
                    returnValue += 1
                }
            }
            result = ""
        }
    }
    return returnValue
}
