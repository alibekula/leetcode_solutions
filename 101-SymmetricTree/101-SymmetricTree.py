# Last updated: 18.12.2025, 16:34:06
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
9        
10        def dfs(left, right):
11            if not left and not right:
12                return True
13            
14            if (not left and right) or (left and not right):
15                return False
16            
17            if left.val != right.val:
18                return False
19            
20            return dfs(left.left, right.right) and dfs(left.right, right.left)
21
22        
23        return dfs(root.left, root.right)
24                