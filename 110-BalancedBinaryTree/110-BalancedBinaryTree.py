# Last updated: 13.08.2025, 16:59:46
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = [True]
        def height(root):
            if not root:
                return 0
        
            left_node = height(root.left)
            if not balanced[0]:
                return 0
            right_node = height(root.right)

            if abs(left_node - right_node) > 1:
                balanced[0] =False
                return 0
            
            return max(left_node, right_node) + 1

        height(root)
        return balanced[0]