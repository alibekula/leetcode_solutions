# Last updated: 12.09.2025, 15:52:00
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, mm=float('-inf'), mx=float('inf')):
            if not node:
                return True
            
            if not dfs(node.left, mm = mm, mx= node.val):
                return False
            
            if not (mm < node.val < mx):
                return False
                
            if not dfs(node.right, mm=node.val, mx=mx):
                return False
            
            return True
        
        return dfs(root)
            
