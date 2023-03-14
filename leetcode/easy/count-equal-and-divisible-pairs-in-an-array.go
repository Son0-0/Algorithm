func countPairs(nums []int, k int) int {
    result := 0

    for i := 0; i < len(nums); i++ {
        for j := i+1; j < len(nums); j++ {
            if nums[i] == nums[j] && (i * j) % k == 0 {
                result++
            }
        }
    }

    return result
}
