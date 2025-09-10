# Last updated: 11.09.2025, 02:01:43
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        min_level = float('inf')

        def dfs(node, level=1):
            nonlocal min_level
            if not node:
                return
            
            if not node.left and not node.right:
                min_level = min(min_level, level)
                return 

            
            dfs(node.left, level+1)
            dfs(node.right, level+1)
        
        dfs(root)

        return min_level if min_level != float('inf') else 0