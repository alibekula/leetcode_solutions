# Last updated: 09.01.2026, 14:44:18
1from collections import deque
2
3class Solution:
4    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
5        
6
7        def dfs(node):
8            if not node:
9                return None, 0
10
11            left, len_left = dfs(node.left)
12            right, len_right = dfs(node.right)
13
14            if len_left > len_right:
15                return left, len_left + 1
16            elif len_right > len_left:
17                return right, len_right + 1
18            else:
19                return node, len_left + 1
20        
21        res, _ = dfs(root)
22        return res
23