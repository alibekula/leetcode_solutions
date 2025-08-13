# Last updated: 13.08.2025, 16:59:50
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        dct = {key: val for val, key in enumerate(inorder) }

        def build_tree(left, right):
            if left > right:
                return None
            
            val = postorder.pop()
            idx = dct[val]
            root = TreeNode(val)

            root.right = build_tree(idx+1, right)
            root.left = build_tree(left, idx-1)

            return root
        
        return build_tree(0, len(postorder)-1)
            
            

        