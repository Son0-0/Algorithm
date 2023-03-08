func isPowerOfTwo(n int) bool {
    for ofs := 0; ofs < 31; ofs++ {
        if n == 1 << ofs {
            return true
        }
    }
    return false
}
