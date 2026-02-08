# Last updated: 08.02.2026, 14:15:19
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isBalanced(self, root: Optional[TreeNode]) -> bool:
9        balanced = [True]
10        def height(root):
11            if not root:
12                return 0
13        
14            left_node = height(root.left)
15            if not balanced[0]:
16                return 0
17            right_node = height(root.right)
18
19            if abs(left_node - right_node) > 1:
20                balanced[0] =False
21                return 0
22            
23            return max(left_node, right_node) + 1
24
25        height(root)
26        return balanced[0]