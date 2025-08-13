# Last updated: 13.08.2025, 16:57:09
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    from collections import deque
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        ans = []

        def bfs(node):
            if not node:
                return 
            
            queue = deque([node, '<level_end>'])
            level_sum = 0
            level_count = 1

            while queue:
                n = queue.popleft()

                if n == '<level_end>':
                    ans.append(level_sum/level_count)

                    if not queue:
                        break
                    else:
                        level_count = len(queue)
                        level_sum = 0
                        queue.append('<level_end>')
                else:
                    level_sum += n.val
                    
                    if n.left:
                        queue.append(n.left)
                    
                    if n.right:
                        queue.append(n.right)
            
        bfs(root)
        return ans

                


            

        