# https://leetcode.com/problems/balanced-binary-tree/
# 110. Balanced Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        answer = True

        def dfs(cur, cnt):
            if not cur:
                return 0

            left = dfs(cur.left, cnt + 1)
            right = dfs(cur.right, cnt + 1)

            if 1 < abs(left - right):
                nonlocal answer
                answer = False

            return max(left, right) + 1

        dfs(root, 0)

        return answer
