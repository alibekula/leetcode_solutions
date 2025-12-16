# Last updated: 16.12.2025, 21:21:47
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
8
9        prev = None
10        curr = head
11
12        while curr:
13            tmp = curr.next
14            curr.next = prev
15            prev = curr
16            curr = tmp
17        
18        return prev
19        