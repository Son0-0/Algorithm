# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
                
        def postorder(preorder, inorder):
            if not preorder or not inorder:
                return None
            
            answer = TreeNode(preorder[0])
            idx = inorder.index(preorder[0])
            answer.left = postorder(preorder[1:idx + 1], inorder[0:idx])
            answer.right = postorder(preorder[idx + 1:], inorder[idx + 1:])
        
            return answer
        
        return postorder(preorder, inorder)