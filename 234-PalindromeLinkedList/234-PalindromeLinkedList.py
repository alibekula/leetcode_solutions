# Last updated: 13.08.2025, 16:58:19
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return True
        
        fast, slow = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev = None

        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node

        left, right = head, prev

        while right:
            if left.val != right.val:
                return False

            left = left.next
            right = right.next

        return True 

        