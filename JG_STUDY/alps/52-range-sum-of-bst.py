# https://leetcode.com/problems/range-sum-of-bst
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        _sum = 0
        
        def inorder(node):
            nonlocal _sum
            
            if not node:
                return 
            
            inorder(node.left)
            if low <= node.val <= high:
                _sum += node.val
            inorder(node.right)
                
        inorder(root)
        
        return _sum