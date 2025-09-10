# Last updated: 11.09.2025, 02:08:44
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        
        queue = deque([root])
        level = 0

        while queue:
            width = len(queue)
            level += 1
            
            for i in range(width):
                node = queue.popleft()
                left = node.left
                right = node.right

                if not left and not right:
                    return level

                if left:
                    queue.append(left)
                
                if right:
                    queue.append(right)

        return 0