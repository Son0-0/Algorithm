func abs(target int) int {
    if target < 0 {
        return -target
    }
    return target
}

func sortedSquares(nums []int) []int {
    result := []int{}

    left, right := 0, len(nums)-1
    
    for left <= right {
        if nums[left] < 0 {
            if nums[right] <= abs(nums[left]) {
                result = append(result, nums[left] * nums[left])
                left++
            } else {
                result = append(result, nums[right] * nums[right])
                right--
            }
        } else {
            break
        }
    }

    for i := right; i >= left; i-- {
        result = append(result, nums[i] * nums[i])
    }

    sort.SliceStable(result, func(a, b int) bool {
        return result[a] < result[b]
    })

    return result
}
