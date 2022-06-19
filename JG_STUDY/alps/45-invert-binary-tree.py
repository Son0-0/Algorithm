# https://leetcode.com/problems/invert-binary-tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(cur):
            if cur:
                dfs(cur.left)
                dfs(cur.right)
                
                cur.left, cur.right = cur.right, cur.left
                
        dfs(root)
        return root
