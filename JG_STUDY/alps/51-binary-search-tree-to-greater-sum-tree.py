# https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        retval = 0
        
        def inorder(root):
            nonlocal retval
            
            if not root:
                return 0
            
            inorder(root.right)
            root.val += retval
            retval = root.val
            inorder(root.left)
        
        inorder(root)
        
        return root
