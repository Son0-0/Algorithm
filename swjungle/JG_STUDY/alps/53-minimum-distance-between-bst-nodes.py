# https://leetcode.com/problems/minimum-distance-between-bst-nodes
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        
        answer = []
        
        def inorder(node):
            nonlocal answer
            
            if not node:
                return
            
            left = inorder(node.left)
            answer.append(node.val)
            right = inorder(node.right)
            
        inorder(root)

        ans = float('inf')
        for idx in range(len(answer) - 1):
            ans = min(ans, abs(answer[idx] - answer[idx + 1]))
        
        return ans