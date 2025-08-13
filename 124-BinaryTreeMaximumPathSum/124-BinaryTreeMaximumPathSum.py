# Last updated: 13.08.2025, 17:30:35
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        max_path = float('-inf')
        def search(node):
            nonlocal max_path
            if not node:
                return
            
            left = search(node.left)
            right = search(node.right)
            left = 0 if not left else left
            right = 0 if not right else right
            max_path = max(max_path, node.val + max(0, left) + max(0 ,right))
            return node.val + max(left, right, 0)

        search(root)
        return max_path 
