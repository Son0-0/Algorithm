# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        answer = 0
        
        if root is None:
            return answer
        
        def dfs(cur, depth):
            nonlocal answer
            
            answer = max(answer, depth)
            
            if cur is None:
                return
            
            if cur.left:
                dfs(cur.left, depth + 1)
            if cur.right:
                dfs(cur.right, depth + 1)
            
        dfs(root, 1)
        
        return answer