# Last updated: 13.08.2025, 16:56:28
class Solution:
    from collections import deque
    def destCity(self, paths: List[List[str]]) -> str:

        if not paths:
            return ''
        
        dct = {}

        for arr, dest in paths:
            dct[arr] = dest
        
        def bfs(root):
            if not root:
                return
            
            queue = deque([root])

            while queue:
                node = queue.popleft()

                if node in dct:
                    queue.append(dct[node])
                else:
                    return node
            
            return -1
        
        return bfs(paths[0][0])


        
