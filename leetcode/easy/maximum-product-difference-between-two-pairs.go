func maxProductDifference(nums []int) int {
    size := len(nums)
    
    sort.Ints(nums)

    return nums[size-1] * nums[size-2] - nums[0] * nums[1]
}
