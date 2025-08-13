# Last updated: 13.08.2025, 16:59:45
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        if not root:
            return False

        def dfs(node, curr):
            if not node:
                return False
            
            if not node.right and not node.left:
                return curr == targetSum
            
            left = node.left.val if node.left else 0
            right = node.right.val if node.right else 0

            return dfs(node.left, curr+left) or dfs(node.right, curr+right)

        return dfs(root, root.val)