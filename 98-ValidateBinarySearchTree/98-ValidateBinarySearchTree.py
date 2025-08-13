# Last updated: 13.08.2025, 16:59:58
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, minimum=float('-inf'), maximum=float('inf')):
            
            if not node:
                return True
            
            if not (minimum < node.val < maximum):
                return False
            
            if not dfs(node.left, minimum=minimum, maximum=node.val):
                return False

            if not dfs(node.right, minimum=node.val, maximum=maximum):
                return False
            
            return True
        

        return dfs(root)