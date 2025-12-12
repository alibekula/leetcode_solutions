# Last updated: 12.12.2025, 20:43:30
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7
8from collections import deque
9class Solution:
10    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
11        if not root:
12            return None
13
14        queue = deque([root])
15
16        while queue:
17            curr = 0
18            width = len(queue)
19
20            for i in range(width):
21                node = queue.popleft()
22                curr += node.val
23
24                if node.left:
25                    queue.append(node.left)
26                
27                if node.right:
28                    queue.append(node.right)
29        
30        return curr
31
32        
33        