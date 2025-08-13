# Last updated: 13.08.2025, 16:57:57
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
        def inner(node):
            if not node:
                return 'N'

            return f"{node.val},{inner(node.left)},{inner(node.right)}"

        return inner(root)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        values = iter(data.split(','))

        def inner():
            val = next(values)

            if val == 'N':
                return None
            
            node = TreeNode(int(val))
            node.left = inner()
            node.right = inner()

            return node
        
        return inner()

            




        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))