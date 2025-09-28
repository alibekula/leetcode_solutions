# Last updated: 28.09.2025, 11:36:25
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        p_found = False
        q_found = False

        p_path = []
        q_path = []


        def dfs(node, path):
            nonlocal p_found, q_found, p, q, p_path, q_path
            if not node or (p_found and q_found):
                return
            path.append(node)

            if node == p:
                p_path = path[:]
                p_found = True
            
            if node == q:
                q_path = path[:]
                q_found = True
            
            dfs(node.left, path)
            dfs(node.right, path)
            path.pop()
        

        dfs(root, [])
        lca = None
        for node1, node2 in zip(p_path, q_path):
            if node1 is node2:
                lca = node1
        
        return lca
