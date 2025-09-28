# Last updated: 28.09.2025, 13:14:32
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        
        prev = node
        curr = node.next
        # 1 2 3 4
        while curr:
            prev.val = curr.val
            curr = curr.next
            if curr:
                prev = prev.next
            else:
                prev.next = None
