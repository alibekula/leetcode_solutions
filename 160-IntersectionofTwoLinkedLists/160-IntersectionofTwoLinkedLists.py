# Last updated: 16.09.2025, 19:20:00
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def get_length(self, head):
        curr = head
        length = 0
        while curr:
            curr = curr.next
            length += 1
        
        return length 

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        lenA = self.get_length(headA)
        lenB = self.get_length(headB)

        if lenA > lenB:
            headA, headB = headB, headA
            lenA, lenB = lenB, lenA
        
        diff = lenB - lenA

        for i in range(diff):
            headB = headB.next
        
        while headA != headB:
            headA = headA.next
            headB = headB.next
        
        return headA