# Last updated: 13.08.2025, 16:57:48
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if not node:
                return (0, 0)
            
            val = node.val
            left = dfs(node.left)
            right = dfs(node.right)

            rob = val + left[0] + right[0]
            not_rob = max(left) + max(right)

            return (not_rob, rob)
        
        return max(dfs(root))