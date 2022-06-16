# https://leetcode.com/problems/diameter-of-binary-tree/
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
        
        def dfs(cur, length):
            if cur is None:
                return length
            
            left_length = dfs(cur.left, length + 1)
            right_length = dfs(cur.right, length + 1)
            
            if left_length and right_length:
                self.answer = max(self.answer, left_length + right_length)
                
        dfs(root, 0)
        print(self.answer)
