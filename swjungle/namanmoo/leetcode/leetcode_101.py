# https://leetcode.com/problems/symmetric-tree/
# 101. Symmetric Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def is_symmetric(left, right):
            if (left == None and right == None):
                return True

            if left != None and right != None:
                if left.val == right.val:
                    return is_symmetric(left.left, right.right) and is_symmetric(left.right, right.left)
            return False

        return is_symmetric(root.left, root.right)
