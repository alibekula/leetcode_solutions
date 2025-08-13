# Last updated: 13.08.2025, 16:58:23
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        curr = 0
        res = None
        def dfs(node):
            nonlocal curr, res
            if not node:
                return
            
            dfs(node.left)
            curr += 1

            if curr == k:
                res = node.val
                return node.val
            
            dfs(node.right)
        
        dfs(root)
        return res