# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def bin_search(left, right):
            if right < left:
                return None
            
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            root.left = bin_search(left, mid - 1)
            root.right = bin_search(mid + 1, right)
            
            return root
            
        return bin_search(0, len(nums) - 1)