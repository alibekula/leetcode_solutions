# Last updated: 09.09.2025, 05:53:14
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverseList(self, root):

        prev = None 
        curr = root

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr

            curr = next_node
        
        return prev





    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return 
        
        fast, slow = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        second = self.reverseList(slow.next)
        slow.next = None

        first = head

        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1

            first, second = tmp1, tmp2
        
