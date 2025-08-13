# Last updated: 13.08.2025, 16:59:54
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    from collections import deque
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        ans = []

        def bfs(node):

            if not node:
                return 
            
            queue = deque([node])

            while queue:
                level = len(queue)
                tmp = []

                for _ in range(level):

                    n = queue.popleft()
                    tmp.append(n.val)

                    if n.left:
                        queue.append(n.left)
                    
                    if n.right:
                        queue.append(n.right)
                
                ans.append(tmp)
        
        bfs(root)

        return ans

            
        