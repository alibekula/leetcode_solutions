# Last updated: 13.08.2025, 16:59:53
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    from collections import deque
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        ans = []
        queue = deque([root])
        left_to_right = True

        while queue:
            level_width = len(queue)
            level = deque()

            for _ in range(level_width):
                node = queue.popleft()

                if left_to_right:
                    level.append(node.val)
                else:
                    level.appendleft(node.val)
                
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)

            ans.append(list(level))
            left_to_right = not left_to_right
        
        return ans

        

        