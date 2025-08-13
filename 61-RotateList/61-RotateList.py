# Last updated: 13.08.2025, 17:00:33
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head:
            return head
        
        if k == 0:
            return head
            
        curr = head
        l = 0
        while curr:
            l += 1
            prev = curr
            curr = curr.next
        
        k %= l
        prev.next = head

        i = l - k
        curr = head
        for _ in range(i-1):
            curr = curr.next
        
        head = curr.next
        curr.next = None

        return head

