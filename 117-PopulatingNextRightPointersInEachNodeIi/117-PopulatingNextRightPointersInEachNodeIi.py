# Last updated: 13.08.2025, 16:59:41
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    from collections import deque
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return 
        
        queue = deque([root, None])

        while queue:
            node = queue.popleft()

            if node:
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            else:
                for i in range(len(queue)-1):
                    queue[i].next = queue[i+1]

                if queue:
                    queue.append(None)
                else:
                    break
        
        return root
                

        