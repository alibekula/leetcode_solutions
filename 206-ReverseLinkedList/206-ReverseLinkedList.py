# Last updated: 12.12.2025, 21:17:48
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
8
9        if not head:
10            return
11
12        prev = None
13        curr = head
14        # 1 -2 -3 -4 -5
15        # 5-4-3-2-1-None
16
17        while curr:
18            tmp = curr.next
19            curr.next = prev
20            prev = curr
21            curr = tmp
22            
23        return prev
24            