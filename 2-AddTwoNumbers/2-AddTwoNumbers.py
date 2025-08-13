# Last updated: 13.08.2025, 17:01:37
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        d = dummy

        while l1 or l2 or carry:

            if l1:
                num1 = l1.val
                l1 = l1.next
            else:
                num1 = 0
            
            if l2:
                num2 = l2.val
                l2 = l2.next
            else:
                num2 = 0
            
            new_num = num1 + num2
            insert_val = (new_num + carry)% 10
            d.next = ListNode(insert_val)
            d = d.next
            carry = (new_num  + carry) // 10
        
        return dummy.next
