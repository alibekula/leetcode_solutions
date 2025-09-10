# Last updated: 11.09.2025, 02:25:34
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(float('-inf'))
        d = dummy
        curr = head

        while curr:
            tmp = d
            while tmp and curr.val > tmp.val:
                prev = tmp
                tmp = tmp.next
            
            if not tmp:
                prev.next = ListNode(curr.val)
            else:
                next_node = prev.next
                prev.next = ListNode(curr.val, tmp)

            curr = curr.next
        
        return dummy.next
