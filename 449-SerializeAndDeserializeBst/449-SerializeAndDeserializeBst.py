# Last updated: 13.08.2025, 16:57:25
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        def dfs(node):
            if not node:
                return 'N'
            
            return f'{node.val},{dfs(node.left)},{dfs(node.right)}'

        return dfs(root)


    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        values = iter(data.split(','))

        def redfs():
            val = next(values)

            if val == 'N':
                return None

            node = TreeNode(int(val))  
            node.left = redfs()
            node.right = redfs()

            return node
        
        return redfs()


# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans