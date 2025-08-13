# Last updated: 13.08.2025, 16:57:20
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        min_diff = float('inf')
        lst = []

        def dfs(node):

            if not node:
                return
            
            dfs(node.left)
            lst.append(node.val)
            dfs(node.right)
        
        dfs(root)
        for i in range(len(lst)-1):
            min_diff = min(min_diff, abs(lst[i] - lst[i+1]))
        
        return min_diff



            
        