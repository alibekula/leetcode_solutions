# Last updated: 13.08.2025, 16:59:47
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    from collections import deque
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:

        def dfs(l, r):
            nonlocal head
            if l > r:
                return

            mid = (l+r)//2

            left = dfs(l,mid-1)
            val = head.val
            head = head.next
            right = dfs(mid+1,r)

            root = TreeNode(val, left, right)

            return root
        
        length = 0
        curr = head

        while curr:
            length += 1
            curr = curr.next

        return dfs(0, length-1)
                

            