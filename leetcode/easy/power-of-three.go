func isPowerOfThree(n int) bool {
    if n == 0 {
        return false
    } else if (n == 1) || (n % 3) == 0 && isPowerOfThree(n / 3) {
        return true
    } else {
        return false
    }
}
