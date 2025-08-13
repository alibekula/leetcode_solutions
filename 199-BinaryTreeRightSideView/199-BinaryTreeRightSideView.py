# Last updated: 13.08.2025, 16:58:53
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    from collections import deque
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def bfs(root):
            if not root:
                return
            
            queue = deque([[root, 1]])
            curr_lvl = 1

            while queue:
                node, lvl = queue.popleft()
                
                if curr_lvl == lvl:
                    ans.append(node.val)
                    curr_lvl += 1
                

                if node.right:
                    queue.append([node.right, lvl+1])
                
                if node.left:
                    queue.append([node.left, lvl+1])

        bfs(root)

        return ans
            

            

        