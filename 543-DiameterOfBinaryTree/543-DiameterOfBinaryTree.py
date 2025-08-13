# Last updated: 13.08.2025, 16:57:19
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.root_diam = 0
        def height(root):
            if not root:
                return 0
            left_node = height(root.left)
            right_node = height(root.right)

            self.root_diam = max(self.root_diam, left_node + right_node)

            return max(right_node, left_node) +1
        height(root)   
        return self.root_diam
            



            


        