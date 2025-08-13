# Last updated: 13.08.2025, 16:57:14
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sub(p, q):
            if not p and not q:
                return True
            
            if not p or not q:
                return False
            
            if p.val != q.val:
                return False
            
            return sub(p.left, q.left) and sub(p.right, q.right)
        
        def subTree(root):
            if not root:
                return 
            
            if sub(root, subRoot):
                return True

            return subTree(root.right) or subTree(root.left)

        return subTree(root)

        