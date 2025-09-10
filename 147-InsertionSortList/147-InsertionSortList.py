# Last updated: 11.09.2025, 02:40:30
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(float('-inf'))
        dummy.next = head
        last_sorted = head
        curr = head.next

        while curr:
            if last_sorted.val <= curr.val:
                last_sorted = curr
            else:
                prev = dummy
                while prev.next and prev.next.val <= curr.val:
                    prev = prev.next
                    
                last_sorted.next = curr.next
                curr.next = prev.next
                prev.next = curr
            curr = last_sorted.next

        return dummy.next
