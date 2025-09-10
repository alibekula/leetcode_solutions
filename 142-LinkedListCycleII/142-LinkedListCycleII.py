# Last updated: 11.09.2025, 04:25:46
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        slow = head
        fast = head
 
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                break
        
        if not fast or not fast.next:
            return 
            
        fast = head

        while fast != slow:
            fast = fast.next
            slow = slow.next
        
        return slow
        

