# Last updated: 13.08.2025, 16:59:49
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def dfs(left, right):
            if left > right:
                return

            idx = (left + right) // 2
            node = TreeNode(nums[idx])
            node.left = dfs(left, idx-1)
            node.right = dfs(idx+1, right)

            return node
        
        return dfs(0, len(nums)-1)
        