# Last updated: 19.09.2025, 21:24:42
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        def dfs(node, path=[], curr = 0):
            nonlocal targetSum
            if not node:
                return 
            
            path.append(node.val)
            curr += node.val

            if curr == targetSum and not (node.left or node.right):
                ans.append(path[:])

            dfs(node.left, path, curr)
            dfs(node.right, path, curr)
            path.pop()
            curr -= node.val

        ans = []
        dfs(root, [], 0)
        return ans
            
