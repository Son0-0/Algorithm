func search(nums []int, target int) int {
    left, right := 0, len(nums)-1
    
    for left <= right {
        mid := (left + right) / 2
        
        if nums[mid] == target {
            return mid
        } else if target < nums[mid] {
            right = mid-1
        } else {
            left = mid+1
        }
    }
    
    return -1
}
