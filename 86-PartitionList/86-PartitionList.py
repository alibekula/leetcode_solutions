# Last updated: 13.08.2025, 17:00:03
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        lesser, greater = ListNode(), ListNode()
        l, r = lesser, greater
        curr = head

        while curr:
            if curr.val < x:
                lesser.next = curr
                lesser = lesser.next
            else:
                greater.next = curr
                greater = greater.next
            
            curr = curr.next
        
        lesser.next = r.next
        greater.next = None

        return l.next
        