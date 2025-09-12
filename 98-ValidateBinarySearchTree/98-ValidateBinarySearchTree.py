# Last updated: 12.09.2025, 08:15:00
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def valid(node):
            if not node:
                return True, float('inf'), float('-inf')

            left_bst, min_left, max_left = valid(node.left)
            right_bst, min_right, max_right = valid(node.right)

            if not left_bst or not right_bst:
                return False, 0, 0
            
            if not (max_left < node.val < min_right):
                return False, 0, 0 
            
            return True, min(node.val, min_left), max(node.val, max_right)

        is_bst, _, _ = valid(root)
        return is_bst  