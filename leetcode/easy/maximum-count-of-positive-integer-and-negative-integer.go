func max(a, b int) int {
    if a < b {
        return b
    }
    return a
}

func maximumCount(nums []int) int {
    p, n := 0, 0

    for _, num := range nums {
        if num < 0 {
            n++
        } else {
            if 0 < num {
                p++
            }
        }
    }

    return max(p, n)
}
