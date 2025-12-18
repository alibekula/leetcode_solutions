# Last updated: 18.12.2025, 18:10:23
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
8        fast = head
9        slow = head
10        prev = head
11        count = 0
12
13        for _ in range(n):
14            fast = fast.next
15        
16        if not fast:
17            return head.next
18
19        while fast:
20            if count >= 1:
21                prev = prev.next
22            count += 1
23            fast = fast.next
24            slow = slow.next
25        
26        prev.next = slow.next
27
28        return head
29        
30