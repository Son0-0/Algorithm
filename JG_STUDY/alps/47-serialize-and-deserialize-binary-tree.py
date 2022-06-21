# https://leetcode.com/problems/serialize-and-deserialize-binary-tree
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        retval = []
        def dfs(cur):
            if not cur:
                retval.append('null')
                return

            retval.append(str(cur.val))

            dfs(cur.left)
            dfs(cur.right)
            
        dfs(root)
        return ' '.join(retval)
                
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(' ')
        ptr = 0
        
        def dfs():
            nonlocal ptr
            if data[ptr] == 'null':
                ptr += 1
                return None
            
            root = TreeNode(int(data[ptr]))
            ptr += 1
            root.left = dfs()
            root.right = dfs()
            return root
        
        return dfs()
        
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))