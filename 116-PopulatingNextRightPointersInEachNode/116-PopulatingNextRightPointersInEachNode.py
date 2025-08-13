# Last updated: 13.08.2025, 16:59:43
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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        if not root:
            return 
            
        head = root
        leftmost = root.left

        while leftmost:

            head.left.next = head.right

            if head.next:
                head.right.next = head.next.left
                head = head.next
            else:
                head = leftmost
                leftmost = head.left

        return root