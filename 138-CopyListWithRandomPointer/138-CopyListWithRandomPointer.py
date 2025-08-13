# Last updated: 13.08.2025, 16:59:21
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(0)
        d = dummy
        dct = {None: None}
        curr = head

        while curr:
            dct[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head

        while curr:

            if curr.next in dct:
                dct[curr].next = dct[curr.next]
            else:
                dct[curr].next = None
            
            if curr.random in dct:
                dct[curr].random = dct[curr.random]
            else:
                dct[curr].random = None
            curr = curr.next
        
        return dct[head]

        
            

            






        