# Last updated: 13.08.2025, 17:00:00
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, l, head):

        prev = None
        tail = head

        while l:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
            l -= 1

        return prev, head, tail

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        if not head or left == right:
            return head
        
        dummy = ListNode()
        dummy.next = head
        curr = dummy

        for i in range(left-1):
            curr= curr.next
        
        start = curr

        new_prev, end, new_tail = self.reverse(right-left+1, curr.next)
        start.next = new_prev
        new_tail.next = end

        return dummy.next

        