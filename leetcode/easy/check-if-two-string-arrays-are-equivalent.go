func arrayStringsAreEqual(word1 []string, word2 []string) bool {
    w1, w2 := "", ""

    for _, w := range word1 {
        w1 += w
    }

    for _, w := range word2 {
        w2 += w
    }

    return w1 == w2
}
