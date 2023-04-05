# https://leetcode.com/problems/merge-two-binary-trees
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        if not root2:
            return root1
        
        def dfs(r1, r2):
            if r1 and r2:
                r1.val += r2.val
                
                if not r1.left and r2.left:
                    r1.left = TreeNode(r2.left.val)
                    r2.left.val = 0
                if not r1.right and r2.right:
                    r1.right = TreeNode(r2.right.val)
                    r2.right.val = 0

                dfs(r1.left, r2.left)
                dfs(r1.right, r2.right)
            
            
        dfs(root1, root2)
        
        return root1