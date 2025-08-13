# Last updated: 13.08.2025, 16:58:46
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        d = dummy

        prev = None 
        tmp = head

        while tmp:
            curr = tmp #1 2
            tmp = tmp.next # 2 3
            curr.next = prev #2 - 1- none
            prev = curr# 2- 1 - None

            # none 1 2 - 3
        return prev
