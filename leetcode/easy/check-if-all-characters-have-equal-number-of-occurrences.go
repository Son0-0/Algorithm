func areOccurrencesEqual(s string) bool {
    dict := make(map[byte]int)

    for _, c := range s {
        dict[byte(c)]++
    }

    cur := dict[s[0]]

    for key := range dict {
        if dict[key] != cur {
            return false
        }
    }

    return true
}
