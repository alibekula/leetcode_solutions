# Last updated: 13.08.2025, 17:01:11
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        heap = []
        dummy = ListNode()
        d = dummy

        for i in range(len(lists)):
            while lists[i]:
                heapq.heappush(heap, lists[i].val)
                lists[i] = lists[i].next

        while heap:
            d.next = ListNode(heapq.heappop(heap))
            d = d.next
        
        return dummy.next