# Last updated: 18.12.2025, 17:01:44
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isValidBST(self, root: Optional[TreeNode]) -> bool:
9
10        if not root:
11            return True
12
13        def dfs(node, arr):
14            if not node:
15                return 
16
17            dfs(node.left, arr)
18            arr.append(node.val)
19            dfs(node.right,arr)
20        
21        seq = []
22        dfs(root, seq)
23
24        if len(seq) == 1:
25            return True
26        
27        n = len(seq)
28
29        for j in range(1, n):
30            i = j-1
31
32            if seq[i] >= seq[j]:
33                return False
34        
35        return True
36        
37
38
39
40        