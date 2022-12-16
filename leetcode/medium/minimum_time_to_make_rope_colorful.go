func minCost(colors string, neededTime []int) int { 
prevColor, prevLength := "", 10001
    result := 0
    
    for idx, color := range colors {
        if string(color) == prevColor {
            if neededTime[idx] <= prevLength {
               result += neededTime[idx]
            } else {
                result += prevLength
                prevLength = neededTime[idx]
            }
        } else {
            prevLength = neededTime[idx]
        }
        prevColor = string(color)
    }
    
    return result
}
