# Last updated: 16.09.2025, 19:45:05
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        branches = []

        def dfs(node, path):
            if not node:
                return

            path.append(node.val)

            if (not node.left and not node.right):
                branches.append(path[:])

            dfs(node.left, path)
            dfs(node.right, path)
            path.pop()
        
        dfs(root, [])

        ans = []
        for branch in branches:
            ans.append('->'.join(map(str, branch)))

        return ans