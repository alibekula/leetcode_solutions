# Last updated: 13.08.2025, 17:00:14
class Solution:
    from math import factorial
    def combine(self, n: int, k: int) -> List[List[int]]:

        total = factorial(n) / (factorial(n-k)*factorial(k))
        ans = []

        def dfs(curr=1, path=None):
            
            path = path if path is not None else []
            if len(path) == k:
                ans.append(path[:])


            if len(ans) == total:
                return 
            
            for num in range(curr, n+1):
                path.append(num)
                dfs(num+1, path)
                path.pop()

        
        dfs()

        return ans
