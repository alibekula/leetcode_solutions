# Last updated: 13.08.2025, 16:59:30
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        lst = []
        def dfs(node, s =''):
            if not node:
                return 
            
            if not node.left and not node.right:
                lst.append(s+f'{node.val}')
                return
            
            dfs(node.left, s+f'{node.val}')
            dfs(node.right, s + f'{node.val}')
        
        dfs(root)

        return sum(map(lambda x: int(x), lst))