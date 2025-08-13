# Last updated: 13.08.2025, 16:59:52
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    longest = 0
    def maxDepth(self, root: Optional[TreeNode], max_d = 0) -> int:
        if not root:
            return max_d
        

        left = self.maxDepth(root.left, max_d + 1)
        right = self.maxDepth(root.right, max_d + 1)

        return max(left, right)
        