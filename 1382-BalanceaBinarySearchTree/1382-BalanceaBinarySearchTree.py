# Last updated: 09.02.2026, 13:17:41
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
9        
10        # 1 2 3 4 5 6 7 8 9 10 11
11        #              6
12        #         3         9
13        #       2  4      8   10
14        #      1     5   7        11
15
16        array = []
17
18        def dfs(node):
19            if not node:
20                return
21            
22            dfs(node.left)
23            array.append(node.val)
24            dfs(node.right)
25
26        dfs(root)
27
28        def build_tree(l, r):
29            if l > r:
30                return None
31
32            mid = (l+r)//2
33            node = TreeNode(array[mid])
34
35            node.left = build_tree(l, mid-1)
36            node.right = build_tree(mid+1, r)
37            return node
38
39        return build_tree(0, len(array)-1)
40
41