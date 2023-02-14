/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func findFrequentTreeSum(root *TreeNode) []int {
    numMap := make(map[int]int)
    
    var inorder func(*TreeNode) int
    
    max := -1
    
    inorder = func(cur *TreeNode) int {
        if cur == nil {
            return 0
        }
        
        sum := cur.Val + inorder(cur.Left) + inorder(cur.Right)
        numMap[sum]++
        
        if max < numMap[sum] {
            max = numMap[sum]
        }
        
        return sum
    }
    
    inorder(root)
    
    result := []int{}
    
    for key := range numMap {
        if numMap[key] == max {
            result = append(result, key)
        }
    }

    return result
}
