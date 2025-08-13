# Last updated: 13.08.2025, 16:58:29
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        curr = 0
        def dfs(node):
            nonlocal curr
            if not node:
                return
            
            curr += 1

            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return curr
            

        