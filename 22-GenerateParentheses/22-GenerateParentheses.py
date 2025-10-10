# Last updated: 10.10.2025, 22:50:11
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def dfs(l, r, path):
            nonlocal n

            if len(path) >= 2*n:
                ans.append(''.join(path))
                return 
            
            if l < n:
                path.append('(')
                dfs(l+1, r, path)
                path.pop()
            
            if r < l:
                path.append(')')
                dfs(l, r+1, path)
                path.pop()
        
        #  ( ( ( )))
        ans = []
        dfs(0, 0, [])
        return ans