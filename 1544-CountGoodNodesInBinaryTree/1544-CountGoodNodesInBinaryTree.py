# Last updated: 12.09.2025, 06:33:18
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        count = 0

        def dfs(node, prev_max=float('-inf')):
            nonlocal count
            if not node:
                return
            
            if node.val >= prev_max:
                count += 1
                
            prev_max = max(prev_max, node.val)
            dfs(node.left, prev_max)
            dfs(node.right, prev_max)
        
        dfs(root)

        return count
        