# https://leetcode.com/problems/longest-univalue-path/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        answer = 0
        
        def dfs(node):
            nonlocal answer
            
            if node is None:
                return 0
            
            left_length = dfs(node.left)
            right_length = dfs(node.right)
            
            if node.left:
                if node.left.val == node.val:
                    left_length += 1
                else:
                    left_length = 0
                
            if node.right:
                if node.right.val == node.val:
                    right_length += 1
                else:
                    right_length = 0
                
            answer = max(answer, left_length + right_length)
            
            return max(left_length, right_length)
                
            
                
                    
        dfs(root)
        
        return answer