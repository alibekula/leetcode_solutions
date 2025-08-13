# Last updated: 13.08.2025, 17:01:15
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        d = dummy

        while list1 or list2:
            
            val1 = list1.val if list1 else float('inf')
            val2 = list2.val if list2 else float('inf')
            
            if val1 <= val2:
                list1 = list1.next
                d.next = ListNode(val1)
            else:
                list2 = list2.next
                d.next = ListNode(val2)
            
            d = d.next

        return dummy.next
