# https://leetcode.com/problems/balanced-binary-tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        flag = 1
        
        def dfs(cur):
            if not cur:
                return 0
            
            left = dfs(cur.left)
            right = dfs(cur.right)
            
            if 1 < abs(left - right):
                nonlocal flag
                flag = 0
                return sys.maxsize
            
            return max(left, right) + 1
        
        dfs(root)
            
        return True if flag == 1 else False