# Last updated: 11.09.2025, 19:37:22
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []
        
        queue = deque([root])
        ans = []

        while queue:
            level = len(queue)
            curr = []

            for i in range(level):
                node = queue.popleft()
                curr.append(node.val)

                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            
            ans.append(curr)
        
        ans.reverse()

        return ans