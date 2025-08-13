# Last updated: 13.08.2025, 16:58:27
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def inv(node):
            if not node:
                return 
            
            left = node.left
            right = node.right
            
            node.right, node.left = left, right

            inv(node.left)
            inv(node.right)

        inv(root)
        return root
        