# Last updated: 15.08.2025, 23:47:45
class Solution:
    def _find_root(self, node):
        if node == self.roots[node]:
            return node
        
        self.roots[node] = self._find_root(self.roots[node])
        return self.roots[node]
    
    def _union(self, node1, node2):
         root1 = self._find_root(node1)
         root2 = self._find_root(node2)

         if root1 != root2:
            self.roots[root2] = root1
            return True
        
         return False
        

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        n = len(edges)
        self.roots = [i for i in range(n+1)]
        ans = []

        for path in edges:
            l, r = path

            if not self._union(l, r):
                ans.append([l, r])
        
        return ans[-1]