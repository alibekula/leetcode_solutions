# Last updated: 13.08.2025, 17:00:09
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        d = dummy

        curr = head

        while curr:
            while curr.next and curr.next.val == curr.val:
                curr = curr.next
            
            if curr == d.next:
                d = d.next
            else:
                d.next = curr.next
            
            curr = curr.next

        return dummy.next