# https://leetcode.com/problems/diameter-of-binary-tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.answer = 0
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def dfs(cur):
            if cur is None:
                return 0
            
            leftlength = dfs(cur.left)
            rightlength = dfs(cur.right)
            self.answer = max(self.answer, leftlength + rightlength)
            
            return max(leftlength, rightlength) + 1
            
        dfs(root)
        return self.answer