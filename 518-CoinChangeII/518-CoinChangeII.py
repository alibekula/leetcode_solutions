# Last updated: 20.08.2025, 20:10:16
class Solution:
    def _find(self, node):
        if self.roots[node] == node:
            return node
        
        self.roots[node] = self._find(self.roots[node])
        return self.roots[node]
    
    def _union(self, node1, node2):
        root1 = self._find(node1)
        root2 = self._find(node2)

        if root1 != root2:
            self.roots[root2] = root1
            return False
        return True
    
    def _is_diff(self, node1, node2):
        root1 = self._find(node1)
        root2 = self._find(node2)

        return root1 != root2

    def equationsPossible(self, equations: List[str]) -> bool:
        
        self.roots = {}

        for s in equations:
            node1, node2 = s[0], s[-1]
            self.roots[node1] = node1
            self.roots[node2] = node2
        
        for s in equations:
            char1 = s[0]
            char2 = s[-1]
            op = s[1:3]

            if op == '==':
                self._union(char1, char2)

        for s in equations:
            char1 = s[0]
            char2 = s[-1]
            op = s[1:3]

            if op == '!=':
                if not self._is_diff(char1, char2):
                    return False
        
        return True

        
        