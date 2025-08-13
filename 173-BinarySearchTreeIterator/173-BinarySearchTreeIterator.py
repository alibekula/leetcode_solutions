# Last updated: 13.08.2025, 16:59:02
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.unwrap(root)

    def unwrap(self, node):

        while node:
            self.stack.append(node)
            node = node.left


    def next(self) -> int:

        top = self.stack.pop()
        val = top.val

        if top.right:
            top = top.right
            while top:
                self.stack.append(top)
                top = top.left
        
        return val

        

    def hasNext(self) -> bool:
        return bool(self.stack)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()