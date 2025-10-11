# Last updated: 11.10.2025, 22:04:47
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        
        if not root:
            return [None]
        
        dct = {}
        ans = []

        def serialise(node):
            if not node:
                return 'N'
            
            left = serialise(node.left)
            right = serialise(node.right)
            key = f'{node.val}/{left}/{right}'

            if key in dct:
                if dct[key] == 1:
                    ans.append(node)
                dct[key] += 1
            else:
                dct[key] = 1
            
            return key
        
        serialise(root)
        return ans
            