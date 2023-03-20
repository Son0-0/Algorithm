func frequencySort(nums []int) []int {
    frequency := make(map[int]int)

    for _, num := range nums {
        frequency[num]++
    }

    sort.Slice(nums, func(i, j int) bool {
        if frequency[nums[i]] < frequency[nums[j]] {
            return true
        } else if frequency[nums[i]] == frequency[nums[j]] {
            if nums[i] > nums[j] {
                return true
            }
        }

        return false
    })

    return nums
}
