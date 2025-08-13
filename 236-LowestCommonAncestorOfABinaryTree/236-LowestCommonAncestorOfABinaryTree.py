# Last updated: 13.08.2025, 16:58:18
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(node, target, path):
            if not node:
                return 
            
            path.append(node)
            if node == target:
                return True
            
            if dfs(node.left, target, path) or dfs(node.right, target, path):
                return True
            
            path.pop()
            return False
        
        path_p, path_q = [], []

        dfs(root, p, path_p)
        dfs(root, q, path_q)
        lca = None

        for p1, q1 in zip(path_p, path_q):
            if p1 == q1:
                lca = p1
        
        return lca
        