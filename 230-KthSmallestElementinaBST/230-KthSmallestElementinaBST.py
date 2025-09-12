# Last updated: 12.09.2025, 17:12:10

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def compute_size(node):
            if not node:
                return 0
            node.size = 1 + compute_size(node.left) + compute_size(node.right)
            return node.size
        
        compute_size(root)

        def search(node, k):
            if not node:
                return None

            left_size = node.left.size if node.left else 0

            if k == left_size + 1:
                return node.val
            elif k <= left_size:
                return search(node.left, k)
            else:
                return search(node.right, k - left_size - 1)
        
        return search(root, k)
